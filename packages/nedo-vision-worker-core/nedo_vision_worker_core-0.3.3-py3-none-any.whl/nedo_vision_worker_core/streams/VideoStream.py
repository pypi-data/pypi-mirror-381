import os
import cv2
import time
import threading
import logging
from typing import Optional, Union, List, Dict
from enum import Enum


# ---------- States ----------
class StreamState(Enum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"
    STOPPED = "stopped"


# ---------- FFmpeg / RTSP tuning (more tolerant; avoids post-keyframe freeze) ----------
def set_ffmpeg_rtsp_env(
    *,
    prefer_tcp: bool = True,
    probesize: str = "256k",
    analyzeduration_us: int = 1_000_000,  # 1s (non-zero)
    buffer_size: str = "256k",
    max_delay_us: int = 700_000,          # 0.7s
    stimeout_us: int = 5_000_000          # 5s socket timeout
) -> None:
    opts = [
        f"rtsp_transport;{'tcp' if prefer_tcp else 'udp'}",
        f"probesize;{probesize}",
        f"analyzeduration;{analyzeduration_us}",
        f"buffer_size;{buffer_size}",
        f"max_delay;{max_delay_us}",
        f"stimeout;{stimeout_us}",
        "flags;low_delay",
        "rtsp_flags;prefer_tcp" if prefer_tcp else "",
        # NOTE: do NOT set reorder_queue_size=0 here; let ffmpeg reorder if needed.
    ]
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "|".join([o for o in opts if o])


# ---------- VideoStream (low-latency, freeze-safe) ----------
class VideoStream(threading.Thread):
    """
    RTSP/file capture that:
      - Primes for first frame (bounded) and immediately enters steady-state.
      - Publishes only the freshest frame (double-buffer).
      - Adds a no-progress watchdog to force reconnect if frames stall.
      - Uses tolerant FFmpeg options to avoid 'first-frame then freeze'.
    """

    def __init__(
        self,
        source: Union[str, int],
        *,
        reconnect_interval: float = 5.0,
        max_failures: int = 5,
        max_reconnect_attempts: int = 10,
        backoff_factor: float = 1.5,
        max_sleep_backoff: float = 60.0,
        target_fps: Optional[float] = None,   # consumer pacing; capture runs free
        enable_backlog_drain: bool = False,   # keep False; can enable later if stable
        ffmpeg_prefer_tcp: bool = True
    ):
        super().__init__(daemon=True)

        # config
        self.source = source
        self.reconnect_interval = reconnect_interval
        self.max_failures = max_failures
        self.max_reconnect_attempts = max_reconnect_attempts
        self.backoff_factor = backoff_factor
        self.max_sleep_backoff = max_sleep_backoff
        self.target_fps = target_fps
        self._drain_backlog = enable_backlog_drain

        # runtime
        self.capture: Optional[cv2.VideoCapture] = None
        self.state: StreamState = StreamState.DISCONNECTED
        self.fps: float = 30.0
        self.frame_count: int = 0
        self.start_time: float = time.time()
        self._running: bool = True

        # first-frame signaling
        self._first_frame_evt = threading.Event()

        # latest-frame (short lock)
        self._latest_frame_lock = threading.Lock()
        self._latest_frame: Optional[cv2.Mat] = None

        # double buffer (very short lock)
        self._buffer_lock = threading.Lock()
        self._buf_a: Optional[cv2.Mat] = None
        self._buf_b: Optional[cv2.Mat] = None
        self._active_buf: str = "a"

        # reconnect backoff
        self._reconnect_attempts = 0
        self._current_interval = reconnect_interval

        # diagnostics
        self._recent_errors: List[Dict[str, Union[str, float]]] = []
        self._max_error_history = 50
        self._codec_info: Optional[str] = None

        # progress watchdog
        self._last_frame_ts: float = 0.0

        # type
        self.is_file = self._is_file_source()

        # set FFmpeg/RTSP options (tolerant profile)
        set_ffmpeg_rtsp_env(prefer_tcp=ffmpeg_prefer_tcp)

    # ----- helpers -----
    def _is_file_source(self) -> bool:
        if isinstance(self.source, int):
            return False
        return isinstance(self.source, (str, bytes, os.PathLike)) and os.path.isfile(str(self.source))

    def _get_source_for_cv2(self) -> Union[str, int]:
        if isinstance(self.source, str) and self.source.isdigit():
            return int(self.source)
        return self.source

    def _initialize_capture(self) -> bool:
        try:
            self.state = StreamState.CONNECTING
            logging.info(f"Connecting to {self.source} (attempt {self._reconnect_attempts + 1})")

            if self.capture:
                self.capture.release()

            self.capture = cv2.VideoCapture(self._get_source_for_cv2(), cv2.CAP_FFMPEG)
            if not self.capture.isOpened():
                logging.error(f"Failed to open video source: {self.source}")
                return False

            self._configure_capture()
            self.state = StreamState.CONNECTED

            # Prime for the first decodable frame (bounded) and immediately step to steady-state
            if not self._prime_until_keyframe(timeout=2.0, max_attempts=30):
                logging.warning("Connected but no initial frame within 2s (waiting for keyframe).")

            return True

        except Exception as e:
            logging.error(f"Error initializing capture: {e}")
            self._cleanup_capture()
            return False

    def _configure_capture(self) -> None:
        # minimal buffering
        try:
            self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        except Exception:
            pass

        # optional timeouts (ignored if unsupported)
        for prop, val in [
            (getattr(cv2, "CAP_PROP_OPEN_TIMEOUT_MSEC", None), 4000),
            (getattr(cv2, "CAP_PROP_READ_TIMEOUT_MSEC", None), 3000),
        ]:
            if prop is not None:
                try:
                    self.capture.set(prop, val)
                except Exception:
                    pass

        # optional HW accel (ignored if unsupported)
        try:
            if hasattr(cv2, "CAP_PROP_HW_ACCELERATION"):
                self.capture.set(cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY)
        except Exception:
            pass

        # fourcc/codec log
        try:
            fourcc = int(self.capture.get(cv2.CAP_PROP_FOURCC))
            if fourcc:
                self._codec_info = "".join([chr((fourcc >> (8 * i)) & 0xFF) for i in range(4)])
                logging.info(f"Stream codec: {self._codec_info} (fourcc: {fourcc})")
        except Exception:
            pass

        detected_fps = self.capture.get(cv2.CAP_PROP_FPS)
        if detected_fps and 0 < detected_fps <= 240:
            self.fps = detected_fps
        else:
            self.fps = 30.0
            logging.warning(f"Unknown/invalid FPS ({detected_fps}); defaulting to {self.fps}")

        if self.is_file:
            total = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
            dur = total / self.fps if self.fps > 0 else 0
            logging.info(f"Video file: {self.fps:.1f} FPS, {int(total)} frames, {dur:.1f}s")
        else:
            logging.info(f"Stream connected at ~{self.fps:.1f} FPS")

    def _cleanup_capture(self) -> None:
        if self.capture:
            try:
                self.capture.release()
            except Exception as e:
                logging.error(f"Error releasing capture: {e}")
            finally:
                self.capture = None
        self.state = StreamState.DISCONNECTED

    def _sleep_interruptible(self, duration: float) -> bool:
        end = time.perf_counter() + duration
        while self._running and time.perf_counter() < end:
            time.sleep(0.05)
        return self._running

    def _handle_reconnection(self) -> bool:
        if self._reconnect_attempts >= self.max_reconnect_attempts:
            logging.error(f"Max reconnection attempts reached for {self.source}")
            return False
        self._reconnect_attempts += 1
        self.state = StreamState.RECONNECTING
        self._current_interval = min(self._current_interval * self.backoff_factor, self.max_sleep_backoff)
        logging.warning(f"Reconnecting in {self._current_interval:.1f}s...")
        return self._sleep_interruptible(self._current_interval)

    def _handle_file_end(self) -> bool:
        if not self.is_file:
            return False
        try:
            cur = self.capture.get(cv2.CAP_PROP_POS_FRAMES)
            total = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
            if cur >= total - 1:
                self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                return True
        except Exception as e:
            logging.error(f"Error handling file end: {e}")
        return False

    # publish freshest
    def _publish_latest(self, frame: cv2.Mat) -> None:
        with self._buffer_lock:
            if self._active_buf == "a":
                self._buf_b = frame
                self._active_buf = "b"
            else:
                self._buf_a = frame
                self._active_buf = "a"
        with self._latest_frame_lock:
            src = self._buf_b if self._active_buf == "b" else self._buf_a
            self._latest_frame = None if src is None else src.copy()
            if not self._first_frame_evt.is_set() and self._latest_frame is not None:
                self._first_frame_evt.set()
        self._last_frame_ts = time.perf_counter()

    # bounded priming + immediate read()
    def _prime_until_keyframe(self, *, timeout: float, max_attempts: int) -> bool:
        deadline = time.perf_counter() + timeout
        attempts = 0
        got = False
        while self._running and time.perf_counter() < deadline and attempts < max_attempts:
            attempts += 1
            if not self.capture.grab():
                time.sleep(0.01)
                continue
            ok, frame = self.capture.retrieve()
            if ok and frame is not None and frame.size > 0:
                self._publish_latest(frame)
                got = True
                break
        if got:
            # immediately step into steady-state
            ret, frame2 = self.capture.read()
            if ret and frame2 is not None and frame2.size > 0:
                self._publish_latest(frame2)
        return got

    # ----- main loop -----
    def run(self) -> None:
        failures = 0
        while self._running:
            try:
                if not self.capture or not self.capture.isOpened():
                    if not self._initialize_capture():
                        if not self._handle_reconnection():
                            break
                        continue
                    # reset counters
                    failures = 0
                    self._reconnect_attempts = 0
                    self._current_interval = self.reconnect_interval

                ret, frame = self.capture.read()

                if not ret or frame is None or frame.size == 0:
                    if self._handle_file_end():
                        continue
                    failures += 1
                    if failures > self.max_failures:
                        logging.error("Too many consecutive read failures; reconnecting.")
                        self._cleanup_capture()
                        failures = 0
                        continue
                    if not self._sleep_interruptible(0.02):
                        break
                    # watchdog: if we’re “connected” but making no progress
                    if self.state in (StreamState.CONNECTED, StreamState.RECONNECTING):
                        if self._last_frame_ts and (time.perf_counter() - self._last_frame_ts) > 2.5:
                            logging.warning("No new frames for 2.5s while CONNECTED; forcing reconnect.")
                            self._cleanup_capture()
                    continue

                # success
                failures = 0
                self.frame_count += 1

                # (optional) backlog drain — disabled by default to avoid freeze
                if self._drain_backlog and not self.is_file and self._first_frame_evt.is_set():
                    # bounded single-drain example (do not loop aggressively)
                    grabbed = self.capture.grab()
                    if grabbed:
                        ok, last = self.capture.retrieve()
                        if ok and last is not None and last.size > 0:
                            frame = last

                self._publish_latest(frame)

                # watchdog: reconnect if no progress despite being connected
                if self.state in (StreamState.CONNECTED, StreamState.RECONNECTING):
                    if self._last_frame_ts and (time.perf_counter() - self._last_frame_ts) > 2.5:
                        logging.warning("No new frames for 2.5s while CONNECTED; forcing reconnect.")
                        self._cleanup_capture()

            except cv2.error as e:
                msg = f"OpenCV error: {e}"
                logging.error(msg)
                self._add_error_to_history(msg)
                self._cleanup_capture()
                if not self._sleep_interruptible(0.5):
                    break

            except Exception as e:
                msg = f"Unexpected error: {e}"
                logging.error(msg, exc_info=True)
                self._add_error_to_history(msg)
                if not self._sleep_interruptible(self.reconnect_interval):
                    break

        self._final_cleanup()

    # ----- public API -----
    def get_frame(self) -> Optional[cv2.Mat]:
        if not self._running or self.state not in (StreamState.CONNECTED, StreamState.RECONNECTING):
            return None
        with self._latest_frame_lock:
            return None if self._latest_frame is None else self._latest_frame.copy()

    def wait_first_frame(self, timeout: float = 5.0) -> bool:
        return self._first_frame_evt.wait(timeout)

    def is_connected(self) -> bool:
        return self.state == StreamState.CONNECTED

    @property
    def running(self) -> bool:
        return self._running and self.state != StreamState.STOPPED

    def get_state(self) -> StreamState:
        return self.state

    def is_video_ended(self) -> bool:
        if not self.is_file or not self.capture:
            return False
        try:
            cur = self.capture.get(cv2.CAP_PROP_POS_FRAMES)
            total = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
            return cur >= total - 1
        except Exception:
            return False

    def stop(self, timeout: float = 5.0) -> None:
        if not self._running:
            return
        logging.info(f"Stopping VideoStream: {self.source}")
        self._running = False
        if self.is_alive():
            self.join(timeout=timeout)
            if self.is_alive():
                logging.warning(f"Stream thread did not exit within {timeout}s")

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    # ----- teardown & diagnostics -----
    def _final_cleanup(self) -> None:
        self.state = StreamState.STOPPED
        self._cleanup_capture()
        with self._latest_frame_lock:
            self._latest_frame = None
        with self._buffer_lock:
            self._buf_a = None
            self._buf_b = None
        logging.info(f"VideoStream stopped: {self.source}")

    def _add_error_to_history(self, error_msg: str) -> None:
        t = time.time()
        self._recent_errors.append({"timestamp": t, "error": error_msg})
        if len(self._recent_errors) > self._max_error_history:
            self._recent_errors = self._recent_errors[-self._max_error_history:]

    def get_recent_errors(self, max_age_seconds: float = 300) -> List[Dict[str, Union[str, float]]]:
        now = time.time()
        return [e for e in self._recent_errors if now - e["timestamp"] <= max_age_seconds]

    def get_codec_info(self) -> Optional[str]:
        return self._codec_info
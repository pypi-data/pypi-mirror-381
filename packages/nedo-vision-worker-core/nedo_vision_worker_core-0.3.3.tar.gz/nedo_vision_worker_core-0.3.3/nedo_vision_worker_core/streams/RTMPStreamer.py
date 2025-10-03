import subprocess
import logging
import threading
import time
import numpy as np
import os
from typing import Optional

class RTMPStreamer:
    """
    Streams raw BGR frames to FFmpeg -> RTMP with:
      - Internal pacing thread (exact fps)
      - Latest-only frame buffer (no backlog)
      - Resilient auto-restart on failure
    """

    def __init__(self, pipeline_id: str, fps: int = 25, bitrate: str = "1500k"):
        self.rtmp_server = os.environ.get("RTMP_SERVER", "rtmp://localhost:1935/live")
        self.rtmp_url = f"{self.rtmp_server}/{pipeline_id}"
        self.fps = max(int(fps), 1)
        self.bitrate = bitrate  # e.g. "1500k"

        # VBV aligned to target bitrate by default (override via env if needed)
        self.maxrate = os.environ.get("RTMP_MAXRATE", self.bitrate)
        self.bufsize = os.environ.get("RTMP_BUFSIZE", f"{self._kbps(self.bitrate) * 2}k")

        self.width: Optional[int] = None
        self.height: Optional[int] = None
        self.ffmpeg_process: Optional[subprocess.Popen] = None
        self.started = False
        self.active = False

        # Writer thread & latest-only buffer
        self._writer_thread: Optional[threading.Thread] = None
        self._stop_evt = threading.Event()
        self._lock = threading.Lock()
        self._latest_frame: Optional[np.ndarray] = None  # last BGR frame set by push_frame()

        # pacing
        self._frame_period = 1.0 / self.fps

    # -------------------- public API --------------------

    def is_active(self) -> bool:
        return bool(self.active and self.ffmpeg_process and self.ffmpeg_process.poll() is None)

    def push_frame(self, frame: np.ndarray):
        """
        Provide a frame to the streamer. The internal writer thread will pick up
        the latest frame at the correct fps. Older frames are dropped.
        """
        if frame is None or getattr(frame, "size", 0) == 0:
            return
        if frame.ndim != 3 or frame.shape[2] != 3:
            return

        # On the very first frame, learn WxH and start ffmpeg + writer
        if not self.started:
            h, w = frame.shape[:2]
            if w <= 0 or h <= 0:
                return
            self.width, self.height = w, h
            self._start_ffmpeg_and_writer()

        # Store latest only
        with self._lock:
            if frame.dtype != np.uint8:
                frame = frame.astype(np.uint8, copy=False)
            if not frame.flags['C_CONTIGUOUS']:
                frame = np.ascontiguousarray(frame)
            self._latest_frame = frame

    def stop_stream(self):
        """Stop writer thread and FFmpeg cleanly."""
        self.active = False
        self._stop_evt.set()

        if self._writer_thread and self._writer_thread.is_alive():
            try:
                self._writer_thread.join(timeout=2.0)
            except Exception as e:
                logging.error(f"RTMP writer thread join error: {e}")
        self._writer_thread = None

        # tear down ffmpeg
        proc = self.ffmpeg_process
        self.ffmpeg_process = None
        if not proc:
            logging.info("RTMP streaming process already stopped.")
            return

        try:
            if proc.stdin:
                try:
                    proc.stdin.flush()
                except Exception:
                    pass
                try:
                    proc.stdin.close()
                except Exception:
                    pass
            proc.terminate()
            proc.wait(timeout=5)
        except Exception as e:
            logging.error(f"Error stopping RTMP stream: {e}")
            try:
                proc.kill()
            except Exception:
                pass
        finally:
            logging.info("RTMP streaming process stopped.")
            self.started = False

    # -------------------- internals --------------------

    def _kbps(self, rate_str: str) -> int:
        return int(str(rate_str).lower().replace("k", "").strip())

    def _build_ffmpeg_cmd(self) -> list[str]:
        # GOP = 1 second for faster recovery; disable scene-cut; repeat headers
        gop = max(self.fps, 1)
        return [
            "ffmpeg",
            "-y",
            "-loglevel", os.environ.get("FFLOG", "error"),
            "-nostats",
            "-hide_banner",

            # raw frames via stdin
            "-f", "rawvideo",
            "-pixel_format", "bgr24",
            "-video_size", f"{self.width}x{self.height}",
            "-framerate", str(self.fps),
            "-i", "-",

            # encoder
            "-c:v", "libx264",
            "-tune", "zerolatency",
            "-preset", "ultrafast",
            "-profile:v", "main",
            "-pix_fmt", "yuv420p",

            # CBR-like VBV
            "-b:v", self.bitrate,
            "-maxrate", self.maxrate,
            "-bufsize", self.bufsize,

            # GOP / keyframes
            "-g", str(gop),
            "-keyint_min", str(gop),
            "-sc_threshold", "0",
            "-x264-params", "open_gop=0:aud=1:repeat-headers=1:nal-hrd=cbr",
            # force an IDR every 1s for faster player join/recovery
            "-force_key_frames", "expr:gte(t,n_forced*1)",

            # single scaling location (if needed downstream)
            "-vf", "scale='min(1024,iw)':-2",

            # no audio
            "-an",

            # reduce container buffering
            "-flvflags", "no_duration_filesize",
            "-flush_packets", "1",
            "-rtmp_live", "live",
            "-muxpreload", "0",
            "-muxdelay", "0",

            "-f", "flv",
            self.rtmp_url,
        ]

    def _start_ffmpeg_and_writer(self):
        """Start ffmpeg process and the pacing writer thread."""
        cmd = self._build_ffmpeg_cmd()
        try:
            with open(os.devnull, "w") as devnull:
                self.ffmpeg_process = subprocess.Popen(
                    cmd,
                    stdin=subprocess.PIPE,
                    stdout=devnull,
                    stderr=devnull if os.environ.get("FFSILENT", "1") == "1" else None,
                    bufsize=0,  # unbuffered for low latency
                )
            self.started = True
            self.active = True
            self._stop_evt.clear()
            self._writer_thread = threading.Thread(
                target=self._writer_loop, name=f"rtmp-writer-{os.getpid()}",
                daemon=True
            )
            self._writer_thread.start()
            logging.info(f"RTMP streaming started: {self.rtmp_url} ({self.width}x{self.height}@{self.fps}fps)")
        except Exception as e:
            logging.error(f"Failed to start FFmpeg: {e}")
            self.ffmpeg_process = None
            self.active = False
            self.started = False

    def _writer_loop(self):
        """Paces frames at exact fps, writing latest frame only. Auto-restarts on failure."""
        next_deadline = time.monotonic() + self._frame_period
        idle_frame: Optional[np.ndarray] = None  # reuse last good frame if no new one arrived

        while not self._stop_evt.is_set():
            try:
                # pacing
                now = time.monotonic()
                sleep_for = next_deadline - now
                if sleep_for > 0:
                    time.sleep(sleep_for)
                next_deadline += self._frame_period
                if next_deadline < now - self._frame_period:
                    next_deadline = now + self._frame_period

                # get the freshest frame
                with self._lock:
                    frame = self._latest_frame

                if frame is None:
                    # no new frame—if we have an idle one, repeat it (prevents RTMP underflow)
                    frame_to_send = idle_frame
                    if frame_to_send is None:
                        continue  # nothing to send yet
                else:
                    frame_to_send = frame
                    idle_frame = frame

                if not self.is_active():
                    raise BrokenPipeError("FFmpeg not active")

                # write raw BGR24
                self.ffmpeg_process.stdin.write(frame_to_send.tobytes())

            except BrokenPipeError:
                # logging.error("RTMP pipe broken. Restarting encoder.")
                self._restart_ffmpeg()
                # On restart we keep width/height; writer will continue
            except Exception as e:
                # Any unexpected error: try a restart, but do not spin
                # logging.error(f"RTMP writer error: {e}")
                time.sleep(0.1)
                self._restart_ffmpeg()

    def _restart_ffmpeg(self):
        """Restart ffmpeg while keeping width/height and thread alive."""
        self.active = False
        proc = self.ffmpeg_process
        self.ffmpeg_process = None
        if proc:
            try:
                if proc.stdin:
                    try:
                        proc.stdin.flush()
                    except Exception:
                        pass
                    try:
                        proc.stdin.close()
                    except Exception:
                        pass
                proc.terminate()
                proc.wait(timeout=3)
            except Exception:
                try:
                    proc.kill()
                except Exception:
                    pass

        # restart only if we have size info
        if self.width and self.height:
            try:
                with open(os.devnull, "w") as devnull:
                    self.ffmpeg_process = subprocess.Popen(
                        self._build_ffmpeg_cmd(),
                        stdin=subprocess.PIPE,
                        stdout=devnull,
                        stderr=devnull if os.environ.get("FFSILENT", "1") == "1" else None,
                        bufsize=0,
                    )
                self.active = True
                # logging.info("RTMP encoder restarted.")
            except Exception as e:
                logging.error(f"Failed to restart FFmpeg: {e}")
                self.active = False
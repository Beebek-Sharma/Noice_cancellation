# Noise_cancellation (Python + WebRTC noise suppression)

This project uses **WebRTC's built-in audio processing** (noise suppression, echo cancellation, auto gain control) without machine learning.

Because the available Python in this workspace is **Python 3.14**, the common pip wrapper for WebRTC Audio Processing Module (APM) does not install cleanly.
So this implementation serves a small web page from Python and performs noise suppression in the browser (Chromium/Firefox). The page uses a local WebRTC loopback call (PeerConnection → PeerConnection) because browsers more consistently apply the WebRTC audio-processing pipeline inside an actual WebRTC call than during direct mic monitoring.

## Run

From this folder:

- Install deps: `D:/Noise_cancellation/.venv/Scripts/python.exe -m pip install -r requirements.txt`
- Start server: `D:/Noise_cancellation/.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000`
- Open: `http://127.0.0.1:8000`

Click **Start**, allow microphone access, and listen to the monitor audio. The `Status` panel shows the requested constraints and the track settings the browser applied.

## Notes

- Noise suppression effectiveness varies by browser/OS/device drivers.
- `noiseSuppression`, `echoCancellation`, and `autoGainControl` are **hints**; browsers may partially apply them.
- This does not "separate" speakers; it reduces background noise/chatter and stabilizes levels.
- In Brave/Chrome, the page also offers a "Chromium advanced" toggle that enables additional non-standard (non-ML) WebRTC processing hints; it can sometimes reduce residual noise a bit.

## Python-only path (optional)

If you install Python **3.11/3.12** on this machine, we can switch the venv and attempt a true Python realtime pipeline using a WebRTC APM wrapper (e.g. `webrtc-audio-processing`) plus `sounddevice`.

# Whispershell 🎙️

A simple local transcription tool for YouTube videos and audio files.
Built on Whisper and yt-dlp. No cloud, no API keys, no fees.

## What it does

- Paste a YouTube URL → downloads audio, transcribes, saves clean .txt
- Paste a local audio file path → transcribes directly
- All transcripts saved automatically to ~/Transcripts/

## Requirements

- Python 3.12+
- ffmpeg
- openai-whisper
- yt-dlp

## Installation

```bash
sudo apt install ffmpeg
pip install openai-whisper --break-system-packages
pip install yt-dlp --break-system-packages
```

## Usage

```bash
python3 whispershell.py
```

Paste a YouTube URL or local file path when prompted. That's it.

## Legal notice

This tool is for personal and educational use only.
Users are responsible for complying with applicable copyright laws
and platform terms of service. The author is not responsible
for how this tool is used.

## License

MIT

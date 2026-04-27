import os
import subprocess

def is_youtube_url(input_string):
    return "youtube.com" in input_string or "youtu.be" in input_string

def transcribe(audio_path):
    print(f"Transcribing: {audio_path}")
    subprocess.run([
        "whisper", audio_path,
        "--language", "English",
        "--output_format", "txt",
        "--output_dir", os.path.expanduser("~/Transcripts")
    ])

def download_youtube(url):
    output_template = os.path.expanduser("~/Downloads/%(title)s.mp3")
    print(f"Downloading: {url}")
    result = subprocess.run([
        "yt-dlp", "-x", "--audio-format", "mp3",
        "--print", "after_move:filepath",
        "-o", output_template, url
    ], capture_output=True, text=True)
    
    audio_path = result.stdout.strip()
    if not audio_path or not os.path.exists(audio_path):
        print("Could not detect file. Check ~/Downloads manually.")
        return
    
    print(f"Downloaded: {audio_path}")
    transcribe(audio_path)

def main():
    os.makedirs(os.path.expanduser("~/Transcripts"), exist_ok=True)
    user_input = input("Paste YouTube URL or local file path: ").strip()
    if is_youtube_url(user_input):
        download_youtube(user_input)
    else:
        transcribe(user_input)

main()

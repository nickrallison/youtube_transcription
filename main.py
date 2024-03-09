# Import necessary libraries
from pytube import YouTube
import os
import sys
import subprocess
import whisper

# Function to download YouTube video
def download_video(url):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    return video.default_filename


# Function to convert video to audio
def convert_video_to_audio(video_filename, audio_filename="audio.wav"):
    command = f"ffmpeg -i {video_filename} -vn {audio_filename}"
    print(command)
    subprocess.call(command, shell=True)
    return audio_filename

def transcribe_audio(audio_filename, model="base"):

    model = whisper.load_model(model)
    result = model.transcribe(audio_filename)
    return result["text"]

def transcribe_url(url, model="base"):
    filename = download_video(url)
    cleaned_filename = filename.replace(" ", "_")
    wav_filename = os.path.splitext(cleaned_filename)[0] + ".wav"
    transcript_filename = os.path.splitext(cleaned_filename)[0] + ".txt"
    os.rename(filename, cleaned_filename)
    convert_video_to_audio(cleaned_filename, wav_filename)
    os.remove(cleaned_filename)
    transcript = transcribe_audio(wav_filename, model)
    os.remove(wav_filename)
    return transcript_filename, transcript


if __name__ == '__main__':
    # From this page: https://pypi.org/project/openai-whisper/
    model = "large"  # tiny, base, small, medium, large
    url = 'https://www.youtube.com/watch?v=IxNib6k5Qno'
    (transcript_filename, transcript) = transcribe_url(url, model)

    base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    output_path = os.path.join(base_path, "output")

    with open(os.path.join(output_path, transcript_filename), "w") as file:
        file.write(transcript)

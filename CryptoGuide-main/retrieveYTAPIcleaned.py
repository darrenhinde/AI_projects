import os
import subprocess
from datetime import datetime, timedelta
import pandas as pd
from googleapiclient.discovery import build
import isodate
from pytube import YouTube
import whisper

# Constants
API_KEY = os.getenv('YOUTUBE_API_KEY')  # Assumes your API key is stored in an environment variable
# api_keytemp = 'AIzaSyDkfR0yXztLgr7VQGnbUO-ZLM6fFvvRCew'
SEARCH_QUERY = 'crypto'
DAYS_AGO = 3
VIDEO_COUNT = 10
FFMPEG_PATH = '/opt/homebrew/bin/ffmpeg'  # Update this path to your ffmpeg installation #/opt/homebrew/bin/ffmpeg

def duration_to_seconds(duration):
    """Convert ISO 8601 duration to seconds."""
    return isodate.parse_duration(duration).total_seconds()

def build_youtube_client(api_key):
    """Build the YouTube client."""
    return build('youtube', 'v3', developerKey=api_key)

def get_published_after(days_ago):
    """Get a datetime string for a date days_ago before the current date."""
    return (datetime.utcnow() - timedelta(days=days_ago)).strftime('%Y-%m-%dT%H:%M:%SZ')

def fetch_videos(youtube, published_after):
    """Fetch video data from YouTube."""
    request = youtube.search().list(
        q=SEARCH_QUERY,
        part='snippet',
        maxResults=VIDEO_COUNT,
        type='video',
        order='date',
        publishedAfter=published_after
    )
    return request.execute()

def download_youtube_video(video_url, save_path='./'):
    """Download a YouTube video as audio."""
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=save_path)
    return out_file

def convert_to_mp3_ffmpeg(video_path):
    """Convert a video file to MP3 using ffmpeg."""
    audio_path = video_path.replace('.mp4', '.mp3')
    command = [FFMPEG_PATH, '-i', video_path, '-vn', '-ab', '128k', '-ar', '44100', '-y', audio_path]
    subprocess.run(command)
    return audio_path

def transcribe_audio(audio_path):
    """Transcribe audio to text using Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

def process_video(video_id):
    """Process a video ID to transcribe its audio."""
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_path = download_youtube_video(video_url)
    audio_path = convert_to_mp3_ffmpeg(video_path)
    transcription = transcribe_audio(audio_path)
    return transcription

def main():
    youtube = build_youtube_client(API_KEY)
    published_after = get_published_after(DAYS_AGO)
    response = fetch_videos(youtube, published_after)

    # Process response to create a DataFrame
    videos_data = []
    for item in response['items']:
        video_id = item['id']['videoId']
        videos_data.append({
            'Video ID': video_id,
            'Title': item['snippet']['title'],
            'Published Date': item['snippet']['publishedAt'],
            'Channel': item['snippet']['channelTitle'],
            'Transcription': process_video(video_id)  # Transcribe each video
        })

    df_videos = pd.DataFrame(videos_data)
    print(df_videos)

    # Optionally, save the DataFrame to a CSV file
    df_videos.to_csv('youtube_crypto_videos.csv', index=False)

if __name__ == "__main__":
    main()

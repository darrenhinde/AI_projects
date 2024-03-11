from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pandas as pd
import isodate

import subprocess

from pytube import YouTube

from moviepy.editor import *
import whisper

# Example function to convert ISO 8601 duration to seconds
def duration_to_seconds(duration):
    return isodate.parse_duration(duration).total_seconds()

# Your API key goes here
api_key = 'AIzaSyDkfR0yXztLgr7VQGnbUO-ZLM6fFvvRCew'




def download_youtube_video(video_url, save_path='./'):
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=save_path)
    return out_file  # Returns the path of the downloaded file



def convert_to_mp3_ffmpeg(video_path):
    audio_path = video_path.replace('.mp4', '.mp3')  # Define the output audio path
    # Specify the full path to ffmpeg here
    command = ['/opt/homebrew/bin/ffmpeg', '-i', video_path, '-vn', '-ab', '128k', '-ar', '44100', '-y', audio_path]
    subprocess.run(command)
    return audio_path




def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Load the Whisper model; choose the model size as needed
    result = model.transcribe(audio_path)
    return result['text']  # Returns the transcribed text

def process_video(video_id):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_path = download_youtube_video(video_url)
    audio_path = convert_to_mp3_ffmpeg(video_path)
    transcription = transcribe_audio(audio_path)
    return transcription

# video_url = "https://www.youtube.com/watch?v=1v2kmFIQlOk"  # Replace this with your YouTube video URL

# # Step 1: Download the YouTube video
# video_path = download_youtube_video(video_url)

# # Step 2: Convert the downloaded video to MP3
# audio_path = convert_to_mp3_ffmpeg(video_path)


# import os
# # Add FFmpeg bin directory to PATH
# os.environ['PATH'] += os.pathsep + '/opt/homebrew/bin'

# # Step 3: Transcribe the audio
# try:
#     transcribed_text = transcribe_audio(audio_path)
#     print(transcribed_text)
# except Exception as e:
#     print(f"An error occurred during transcription: {e}")


# print(transcribed_text)



## ONE TIME THING

# df_videos.loc[0, 'Transcription'] = transcribed_text




def main():
    
    
    # Build the YouTube client
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Define a datetime object for 3 days ago from now
    three_days_ago = datetime.utcnow() - timedelta(days=3)
    
    # Format the datetime object to RFC 3339 format
    published_after = three_days_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Perform a search query
    request = youtube.search().list(
        q='crypto',
        part='snippet',
        maxResults=10,
        type='video',
        order='date',
        publishedAfter=published_after
    )
    
    # Execute the request and get the response
    response = request.execute()
    
    # Initialize a list to store data
    videos_data = []
    
    # Loop through items and get video details
    for item in response['items']:
        video_id = item['id']['videoId']
        channel_id = item['snippet']['channelId']
        video_title = item['snippet']['title']
        channel_title = item['snippet']['channelTitle']
        publish_date = item['snippet']['publishedAt']
    
        # Get video statistics
        video_request = youtube.videos().list(
            part="statistics,contentDetails",
            id=video_id
        )
        video_response = video_request.execute()
        video_stats = video_response['items'][0]['statistics']
        video_details = video_response['items'][0]['contentDetails']
    
        # Get channel statistics
        channel_request = youtube.channels().list(
            part="statistics",
            id=channel_id
        )
        channel_response = channel_request.execute()
        channel_stats = channel_response['items'][0]['statistics']
    
        # Extract statistics
        view_count = video_stats.get('viewCount', '0')
        like_count = video_stats.get('likeCount', '0')
        subscriber_count = channel_stats.get('subscriberCount', '0')
    
    
        duration = video_details.get('duration', 'PT0S')  # Default to PT0S if not found
        duration_seconds = duration_to_seconds(duration)
    
        # Append data to list
        videos_data.append([
            video_title, video_id, view_count, like_count,
            publish_date, channel_title, subscriber_count, duration_seconds
        ])
    
    
    # Convert list to DataFrame
    columns = [
        'Title', 'Video ID', 'Views', 'Likes',
        'Published Date', 'Channel', 'Subscribers', 'Duration'
    ]
    df_videos = pd.DataFrame(videos_data, columns=columns)
    
    # Display the DataFrame
    print(df_videos)
    
    # Optionally, save the DataFrame to a CSV file
    df_videos.to_csv('youtube_crypto_videos2.csv', index=False)
    
    
    
    df_videos['Transcription'] = ''
    
    
    
    
    # # JUST TEMPORARILY READING THE DATAFRAME
    
    # import pandas as pd
    
    # # Assuming the csv file is in the same directory as your script
    # file_path = "youtube_crypto_videos.csv"
    
    # # Read the csv file into a pandas DataFrame
    # df_videos = pd.read_csv(file_path)
    
    # # Now df_videos contains your data
    
    
    
    
    # FILTER Out LIVE STREAMING VIDEOs.... they will have a duration of 0.
    df_videos = df_videos[df_videos['Duration'] != 0]
    
    df_videos = df_videos[df_videos['Duration'] <= 600]

    
    # MININUMVIABLE PRODUCT: IF VIDEO IS LONGER THAN 600 SECONDS. WE FILTER IT OUT.
    
    
    
    
    df_videos_trimmed = df_videos.head(1)
    # second_row = df_videos.iloc[3:4] 
    



main()


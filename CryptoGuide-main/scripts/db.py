from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

#title, video ID, views, likes, published date, channel, subscribers, transcription
def add_to_video_data(title,video_id,views,likes,p_date,channel_name,subscribers,transcription):
    load_dotenv()

# Use the environment variable
    uri = "mongodb+srv://whitewater:4LWpNZFBrYV8iyF0@cluster0.onfbu8r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Select your database
    db = client['Cryptodata']

    # Select your collection
    collection = db['youtube_sum']

    # Document to insert
    document = {
        "title": title,
        "ID": video_id,
        "views": views,
        "likes": likes,
        "published": p_date,
        "channel": channel_name,
        "subscribers": subscribers,
        "transcription": transcription
    }

    # Insert a single document
    try:
        collection.insert_one(document)
        print("Document inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_to_something_data(name, time, frequency, sentiment, sum):
    load_dotenv()

# Use the environment variable
    uri = "mongodb+srv://whitewater:4LWpNZFBrYV8iyF0@cluster0.onfbu8r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Select your database
    db = client['Cryptodata']

    # Select your collection
    collection = db['crypto_stats']

    document = {
        "name": name,
        "time": time,
        "frequency": frequency,
        "sentiment": sentiment,
        "sum": sum,

    }
        # Insert a single document
    try:
        collection.insert_one(document)
        print("Document inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_to_crypto_data(crypto, views, score):
    load_dotenv()

# Use the environment variable
    uri = "mongodb+srv://whitewater:4LWpNZFBrYV8iyF0@cluster0.onfbu8r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Select your database
    db = client['Cryptodata']

    # Select your collection
    collection = db['crypto_stats']

    document = {
        "crypto": crypto,
        "views": views,
        "score": score
    }
        # Insert a single document
    try:
        collection.insert_one(document)
        print("Document inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_to_summary(title, id, summary):
    load_dotenv()

# Use the environment variable
    uri = "mongodb+srv://whitewater:4LWpNZFBrYV8iyF0@cluster0.onfbu8r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Select your database
    db = client['Cryptodata']

    # Select your collection
    collection = db['summary']

    document = {
        "title": title,
        "id": id,
        "summary": summary
    }
        # Insert a single document
    try:
        collection.insert_one(document)
        print("Document inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



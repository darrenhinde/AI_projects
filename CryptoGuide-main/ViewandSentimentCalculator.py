#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:07:43 2024

@author: brandonslockey
"""


import pandas as pd
from openai import OpenAI
import json
import sys
sys.path.append('/scripts')
import scripts.db as db


client = OpenAI(
    api_key = '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',
    )

def get_crypto_from_transcription(transcript):
    with open('EngineeredPromptv1.txt', 'r') as file:
        prompt_text = file.read().strip()
        
    full_prompt = f"{prompt_text}\n\nTranscript: {transcript}"  # Combine the prompt text with the transcript
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": full_prompt,  # Use the combined prompt here
            }
        ],
        model="gpt-4",  # Specify the model you are using, e.g., "gpt-4"
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return response.choices[0].message.content.strip()
 


    

# Assuming the csv file is in the same directory as your script
file_path = "TestDataSet.csv"

# Read the csv file into a pandas DataFrame
df_of_transcripts = pd.read_csv(file_path)
# Assuming df_of_transcripts has a column 'Transcript' containing the text for GPT to process.
df_of_transcripts['GPT OUTPUT'] = df_of_transcripts['Transcriptions'].apply(get_crypto_from_transcription)

    

    
df_of_transcripts.to_csv('GPTOUTPUTS.csv', index=False)























# Example initialization of df_of_transcripts
# df_of_transcripts = pd.DataFrame({
#     'VideoViews': [3000, 6000],
#     'GPTOutput': ['your_json_string_here_for_each_row', 'another_json_string_here']
# })

# Initialize an empty list to store the aggregated data
aggregated_data = []

# Iterate through each row in the df_of_transcripts DataFrame
# Assuming 'Video ID' is a column in df_of_transcripts
for _, row in df_of_transcripts.iterrows():
    gpt_output = json.loads(row['GPT OUTPUT'])
    views = row['Views']
    video_id = row['Video ID']
    published_date = row['Published Date']  # Retrieve the Published Date from the current row
    
    for crypto, details in gpt_output['cryptocurrencies'].items():
        aggregated_data.append({
            'Video ID': video_id,
            'Cryptocurrency': crypto,
            'Views': views,
            'SentimentScore': details['sentiment_score'],
            'Published Date': published_date  # Include Published Date in the data being appended
        })


# Convert the aggregated data list into a DataFrame
sentiment_frequency_dataframe = pd.DataFrame(aggregated_data)

# If you want to sum views for each cryptocurrency and get the average sentiment score,
# you can group by the Cryptocurrency column and aggregate accordingly
final_df = sentiment_frequency_dataframe.groupby('Cryptocurrency').agg({
    'Views': 'sum',
    'SentimentScore': 'mean'
}).reset_index()

# Display the final DataFrame
#print(final_df)
db.add_to_crypto_data(final_df["Cryptocurrency"], final_df["Views"], final_df["SentimentScore"])


    
    



# Now df contains your data from the CSV file

    
# def main():
# if __name__ == "__main__":
#     main()

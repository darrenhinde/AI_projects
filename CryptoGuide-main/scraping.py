import pandas as pd
import json
import sys
sys.path.append('/scripts')
import scripts.db as db

df_of_transcripts = pd.read_csv('GPTOUTPUTS.csv')

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
def scrape():
    for index, row in final_df.iterrows():
        db.add_to_crypto_data(row["Cryptocurrency"], row["Views"], row["SentimentScore"])

    
    


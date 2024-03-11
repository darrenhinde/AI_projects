import pandas as pd
import json
import db

def print_video_details(input_file_path):
    df = pd.read_csv(input_file_path)

    for index, row in df.iterrows():
        # Parse the JSON from the "GPT OUTPUT" column
        gpt_output = json.loads(row['GPT OUTPUT'])
        
        # Extract the Bitcoin summary or adapt this to extract the relevant part
        summary = gpt_output.get('cryptocurrencies', {}).get('Bitcoin', {}).get('summary', 'No summary found')

        # Print the details
        try:
            db.add_to_summary(row['Title'], row['Video ID'], summary)
        except UnicodeEncodeError as e:
            # Handle potential unicode errors during print
            print(f"Failed to print row {index} due to encoding issues: {e}")

        

# Example usage
input_file_path = "GPTOUTPUTS2.csv"
print_video_details(input_file_path)




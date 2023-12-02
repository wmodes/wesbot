"""
generate_embeddings.py - Generate embeddings for text data

Author: Wes Modes
Date: 2023

Notes: based on the OpenAI cookbook recipe "Question answering using embeddings-based search"
https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb
"""

# imports
import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
import tiktoken  # for counting tokens
from scipy import spatial  # for calculating vector similarities for search
import sys
sys.path.append('..')
import config
import mysecrets



# Set your API key and organization
openai.api_key = mysecrets.OPENAI_API_KEY
openai.organization = config.OPENAI_ORG

# models
EMBEDDING_MODEL = "text-embedding-ada-002"

# files
SOURCE_FILE = "../training/source/f_entity.csv"
EMBEDDINGS_FILE = "../training/embeddings/f_entity.csv"

# This is costly so we only want to do this as necessary
# 
# Compare the "data" field in the source file to the "text" field in the embeddings file
# If they are the same, we can skip this step

# Load the source file and the embeddings file into DataFrames
source_df = pd.read_csv("../training/source/f_entity.csv")
embeddings_df = pd.read_csv("../training/embeddings/f_entity.csv")

# Sort both DataFrames based on the 'data' and 'text' columns respectively
source_df.sort_values(by='data', inplace=True)
embeddings_df.sort_values(by='text', inplace=True)

# Resetting the index to align rows for comparison
source_df.reset_index(drop=True, inplace=True)
embeddings_df.reset_index(drop=True, inplace=True)

# Check if the embeddings file exists and has data
if not embeddings_df.empty:
    # Assuming the "data" and "text" fields are in the respective DataFrames
    source_data = source_df['data'].astype(str)  # Convert 'data' column to string for comparison
    embeddings_text = embeddings_df['text'].astype(str)  # Convert 'text' column to string for comparison
    
    # Compare 'data' from the source file with 'text' from the embeddings file
    if source_data.equals(embeddings_text):
        print("Embeddings for this data already exist. Saving time and resources and skipping this step.")
        # Exit the script or perform necessary actions here
        exit(0)

print ("Embeddings for this data do not exist. Generating embeddings.")

# If they are different, we need to generate embeddings for the new data
# this portion of the script is already created

# Load the CSV file into a DataFrame
df = pd.read_csv(SOURCE_FILE)

# Extract all values from the 'data' column into an array
data_array = df['data'].tolist()

# Define an array that can store the embeddings
embeddings = []

# Iterate over each cell in the 'data' column
for index in range(len(data_array)):
    # print(data_cell) 
    response = openai.Embedding.create(model=EMBEDDING_MODEL, input=data_array[index])
    for i, be in enumerate(response["data"]):
        assert i == be["index"]  # double check embeddings are in same order as input
    batch_embeddings = [e["embedding"] for e in response["data"]]
    embeddings.extend(batch_embeddings)

df = pd.DataFrame({"text": data_array, "embedding": embeddings})
# print(df)

# Save the DataFrame to a CSV file
df.to_csv(EMBEDDINGS_FILE, index=False)

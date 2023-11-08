"""
json2csv.py - Convert JSON to CSV
"""

import sys
import json
import csv

# Define the fieldnames for the CSV
fieldnames = ["topic", "system", "user", "assistant"]

# Create a CSV writer for stdout
csv_writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, delimiter='\t')
csv_writer.writeheader()

# Read JSON data from stdin
data = json.load(sys.stdin)

# Process each message in the JSON data
for message in data:
    system_content = message["messages"][0]["content"]

    # Extract user and assistant messages
    user_messages = [msg["content"] for msg in message["messages"] if msg["role"] == "user"]
    assistant_messages = [msg["content"] for msg in message["messages"] if msg["role"] == "assistant"]

    # Check for linefeeds and replace with \n
    system_content = system_content.replace('\n', '\\n')
    user_messages = [msg.replace('\n', '\\n') for msg in user_messages]
    assistant_messages = [msg.replace('\n', '\\n') for msg in assistant_messages]

    # Create a record for the first user/assistant message
    if user_messages and assistant_messages:
        csv_writer.writerow({
            "topic": "classes",
            "system": system_content,
            "user": user_messages[0],
            "assistant": assistant_messages[0]
        })

    # Create separate records for additional user/assistant messages
    for user_msg, assistant_msg in zip(user_messages[1:], assistant_messages[1:]):
        csv_writer.writerow({
            "topic": "classes",
            "system": system_content,
            "user": user_msg,
            "assistant": assistant_msg
        })

# Make sure to close the stdout
sys.stdout.close()

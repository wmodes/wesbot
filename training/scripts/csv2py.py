"""
csv2py.py - Converts CSVs file to JSON-like Python data structures and creates new Python files

Converts all the CSV files in the SOURCE_DIR to Python data structures and creates new Python files.

Author: Wes Modes
Date: 2023
"""

import sys
import csv
import os
import re
sys.path.append('..')
import config

# Define folders
BASE_DIR = config.BASE_DIR
SOURCE_DIR = config.SOURCE_DIR  # Use SOURCE_DIR from config

# Define exclusions
FILE_EXCLUDE_REGEX = re.compile(r'^f_', re.IGNORECASE)

file_template = """
import sys
sys.path.append('../')
sys.path.append('../../')
from config import SYSTEM_MSGS

sys_content = SYSTEM_MSGS['{filebase}']

DATA = [
{records}
]
"""

content_template = """
{{
    "messages": [
        {{
            "role": "system",
            "content": sys_content
        }}, {{
            "role": "user",
            "content": \"\"\"{user}\"\"\"
        }}, {{
            "role": "assistant",
            "content": \"\"\"{assistant}\"\"\"
        }}
    ]
}},
"""

function_template = """
{{
    "messages": [
        {{
            "role": "system",
            "content": sys_content
        }}, {{
            "role": "user",
            "content": \"\"\"{user}\"\"\"
        }}, {{
            "role": "assistant",
            "function_call": {{  
                "name": "{function}",
                "arguments": "{arguments}"
            }}
        }}
    ]
}},
"""

def process_csv_file(csv_file_path):
    # Initialize records variable to store record templates
    records = []

    # Read the CSV file and generate record templates
    with open(csv_file_path, newline='') as csvfile:
        # Extract the filename minus the extension and path
        filebase = os.path.splitext(os.path.basename(csv_file_path))[0]

        # Initialize the CSV reader with quoting set to csv.QUOTE_ALL
        reader = csv.DictReader(csvfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            user_content = row['user'].replace('"', r'\"').replace(r'\\"', r'\"')
            assistant_content = row['assistant'].replace('"', r'\"').replace(r'\\"', r'\"')
            
            if user_content and assistant_content:
                # Check if the assistant record starts with "function_call: "
                # Check if "function" is one of the fields in the CSV file
                if "function" in row and row['function']:
                    function = row['function']
                    arguments = row['arguments'].replace('"', r'\"').replace(r'\\"', r'\"')
                    records.append(function_template.format(
                        user=user_content,
                        function=function,
                        arguments=arguments
                    ))
                else:
                    records.append(content_template.format(
                        user=user_content,
                        assistant=assistant_content
                    ))

        # Create the data content with {filebase} replaced
        data_content = file_template.format(filebase=filebase, records="".join(records))

        # Create the Python file path based on the CSV file path
        python_file_path = os.path.splitext(csv_file_path)[0] + ".py"

        # Write the Python file
        with open(python_file_path, 'w') as python_file:
            python_file.write(data_content)

# Process all CSV files in the SOURCE_DIR
for root, dirs, files in os.walk(SOURCE_DIR):
    for filename in files:
        # if it's a CSV file and not in exclusions
        if filename.endswith(".csv") and not FILE_EXCLUDE_REGEX.match(filename):
            csv_file_path = os.path.join(root, filename)
            # Print the filename being processed
            print(f"Processing {filename}...")
            process_csv_file(csv_file_path)

# Print a message indicating the conversion is complete
print("CSV to Python conversion and file creation completed.")

"""
py2jsonl.py - Format data from a Python file to JSONL

Author: Wes Modes
Date: 2023
"""

import json
import os
import sys
sys.path.append('..')
import config
from helpers import super_strip

# Define folders
BASE_DIR = config.BASE_DIR
SOURCE_DIR = config.SOURCE_DIR
DATA_DIR = config.DATA_DIR

def process_input(input_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        sys.exit(1)

def extract_data_from_python(input_content):
    """
    Extract the data structure from the Python file.
    """
    try:
        # Create a dictionary with a placeholder for DATA
        data_dict = {"DATA": None}
        # Safely evaluate the content as a Python object
        exec(input_content, data_dict)
        data = data_dict.get("DATA")
        if data is None:
            raise ValueError("Input file does not contain a variable named 'DATA'.")
        if not isinstance(data, list):
            raise ValueError("'DATA' variable is not a list.")
        return data
    except (SyntaxError, ValueError) as e:
        print(f"Format error in input file: {input_file}\n\t{e}")
        sys.exit(1)

def format_jsonl_content(data):
    """
    Format the data structure from the Python file as JSONL.
    """
    formatted_jsonl = ""
    # go through each record in the data
    for item in data:
        # go through each message in the record
        for message in item['messages']:
            if "function_call" in message:
                # Remove extra spaces and escapes
                function_call = message['function_call']
                message['function_call'] = function_call
            else:
                # print(f"before: {message['content']}")
                message['content'] = super_strip(message['content'])
                # print(f"after: {message['content']}")

        formatted_jsonl += json.dumps(item, ensure_ascii=False) + '\n'

    return formatted_jsonl

def python_to_jsonl(input_file, output_file):
    input_content = process_input(input_file)
    data = extract_data_from_python(input_content)
    formatted_jsonl = format_jsonl_content(data)

    try:
        with open(output_file, 'w') as jsonl_file:
            jsonl_file.write(formatted_jsonl)
        print(f"Conversion completed. JSONL data saved to {output_file}")
    except FileNotFoundError:
        print(f"Output file '{output_file}' not found.")

if __name__ == "__main__":
    # Get a list of .py files in SOURCE_DIR
    py_files = [file for file in os.listdir(SOURCE_DIR) if file.endswith(".py")]

    for py_file in py_files:
        input_file = os.path.join(SOURCE_DIR, py_file)
        output_file = os.path.join(DATA_DIR, os.path.splitext(py_file)[0] + ".jsonl")
        python_to_jsonl(input_file, output_file)
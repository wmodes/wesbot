"""
make_lookup.py - A Python script for generating lookup dictionaries.

Author: Wes Modes
Date: 2023
"""

import csv
import json
import os
import sys
from collections import defaultdict
sys.path.append('..')
import config

# Define folders
BASE_DIR = config.BASE_DIR
SOURCE_DIR = config.SOURCE_DIR
DATA_DIR = config.DATA_DIR


def load_csv_records(file_path):
    """
    Load records from a CSV file.
    """
    records = []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records

def generate_lookup_dicts(source_directory):
    """
    Generate lookup index and contents dictionaries from CSV files.
    """
    lookup_index = defaultdict(list)
    lookup_contents = {}

    # Retrieve all files in SOURCE_DIR that match the pattern f_*.csv
    matching_files = [filename for filename in os.listdir(source_directory) if filename.startswith('f_') and filename.endswith('.csv')]

    # Retrieve all records from these files and put them in a list lookup_records
    lookup_records = []
    for file_name in matching_files:
        file_path = os.path.join(source_directory, file_name)
        records = load_csv_records(file_path)
        lookup_records.extend(records)

    # Go through all the records in lookup_records
    for record in lookup_records:
        entity = record.get('entity')
        data = record.get('data')

        # Convert data string to JSON object if possible
        try:
            data_json = json.loads(data)
        except json.JSONDecodeError:
            data_json = None

        # Access 'name' and 'aka' keys from the converted JSON object
        if data_json and isinstance(data_json, dict):
            name_data = data_json.get('name')
            aka_data = data_json.get('aka')
        else:
            name_data = None
            aka_data = None

        # Create an index dict "lookup_index" for "name" and "aka" in "data" to the "entity" if name_data or aka_data exist
        if name_data:
            lookup_index[entity.lower()] = entity.lower()
            lookup_index[name_data.lower()] = entity.lower()
        if aka_data:
            if isinstance(aka_data, str):
                lookup_index[aka_data.lower()] = entity.lower()
            elif isinstance(aka_data, list):
                for aka_item in aka_data:
                    lookup_index[aka_item.lower()] = entity.lower()

        # Create a lookup dict "lookup_contents" using "name" as the key and "data" as the value
        if entity and data:
            lookup_contents[entity.lower()] = data

    return lookup_index, lookup_contents

def write_lookup_files(lookup_index, lookup_contents):
    """
    Write the index and contents dictionaries to separate Python files.
    """
    with open(os.path.join(DATA_DIR, 'lookup_index.py'), 'w') as index_file:
        index_file.write(f'lookup_index = {json.dumps(lookup_index, indent=4)}')

    with open(os.path.join(DATA_DIR, 'lookup_contents.py'), 'w') as contents_file:
        contents_file.write(f'lookup_contents = {json.dumps(lookup_contents, indent=4)}')

if __name__ == "__main__":
    lookup_index, lookup_contents = generate_lookup_dicts(SOURCE_DIR)

    # Write two files, one for lookup_index.py and one for lookup_contents.py
    write_lookup_files(lookup_index, lookup_contents)

    # Report the results
    print("Lookup index and contents dictionaries created and saved as lookup_index.py and lookup_contents.py.")
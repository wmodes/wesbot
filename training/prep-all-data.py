"""
compile-data.py - reformat data for training, compile into a single file, split into train and test sets, and check the data

This file contains the code for reformatting the data for training, compiling it into a single file, splitting it into train and test sets, and checking the data.

Author: Wes Modes
Date: 2023
"""

# Import required modules
import subprocess
import os

# Config globals

# Root directory of the project
ROOT_DIR = "/Users/wmodes/dev/wesbot"
# Training directory
TRAINING_DIR = f"{ROOT_DIR}/training"

# Data directories
#
# Source directory
SOURCE_DIR = f"{TRAINING_DIR}/source"
# Path to the data directory
DATA_DIR = f"{TRAINING_DIR}/data"
# Path to final data file
FINAL_DATA = f"{DATA_DIR}/data.jsonl"
# Path to lookup dir
LOOKUP_DIR = f"{ROOT_DIR}/lookup"

# Script directories
#
# Script directory
SCRIPT_DIR = f"{TRAINING_DIR}/scripts"
# Script to get data from sheets
SHEETS2CSV_SCRIPT = f"{SCRIPT_DIR}/sheets2csv.py"
# Script to convert CSV data
CSV2PY_SCRIPT = f"{SCRIPT_DIR}/csv2py.py"
# Script to format the data
PY2JSONL_SCRIPT = f"{SCRIPT_DIR}/py2jsonl.py"
# Script to compile the data
CONCATENATE_SCRIPT = '/bin/cat'
# Script to split the data
SPLIT_DATA_SCRIPT = f"{SCRIPT_DIR}/split-data.py"
# Script to check the data
CHECK_SCRIPT = f"{SCRIPT_DIR}/check-data.py"

# extensions for training data files
CSV_EXT = "csv"
PY_EXT = "py"
DATA_EXT = "jsonl"

# Get the csv files from google sheets
print("\n# GETTING DATA FROM SHEETS")
subprocess.run(['python', SHEETS2CSV_SCRIPT])

# Make a list of the csv files minus their extension
CSV_LIST = [file_name for file_name in os.listdir(SOURCE_DIR) if file_name.endswith(f".{CSV_EXT}")]
# Remove the extension from each file name
FILE_LIST = [os.path.splitext(file_name)[0] for file_name in CSV_LIST]

# Convert the csv files to python data files
print("\n# CONVERTING CSV FILES TO PYTHON DATA FILES")
subprocess.run(['python', CSV2PY_SCRIPT])

# Convert Python data files to JSONL
print("\n# CONVERTING PYTHON DATA FILES TO JSONL")
subprocess.run(['python', PY2JSONL_SCRIPT])

# Compile all the data files into a single file
#   cat common.jsonl discord.jsonl email.jsonl email2.jsonl > data.jsonl
print("\n# COMPILING DATA FILES INTO SINGLE FILE")
compiled_files = []
for data_file in FILE_LIST:
    # Modify the extension to DATA_EXT
    data_file_with_ext = data_file + f".{DATA_EXT}"
    # Create the full path and add it to the list
    compiled_file_path = os.path.join(DATA_DIR, data_file_with_ext)
    compiled_files.append(compiled_file_path)
# Construct the concatenate command
compile_command = [CONCATENATE_SCRIPT] + compiled_files
# Join the file paths into a single command string
compile_command_str = ' '.join(compile_command)
# Use shell=True to execute the command
subprocess.run(compile_command_str, shell=True, stdout=open(FINAL_DATA, 'w'))
print(f"Compiled files: {compiled_files}")

# Split the data file into training and test sets
#  py scripts/split-data.py data/data.jsonl 10
print("\n# SPLITTING DATA INTO TRAINING AND TEST SETS")
subprocess.run(['python', SPLIT_DATA_SCRIPT, FINAL_DATA, "10"])

# Check the data file
#   python check-data.py data/data.jsonl
print("\n# CHECKING DATA")
check_command = ['python', CHECK_SCRIPT, FINAL_DATA]
subprocess.run(check_command)

# Run make_lookup.py script and move the generated files to the data directory
#   py scripts/make_lookup.py
#   mv data/lookup*.py ../data/
print("\n# GENERATING LOOKUP FILES")
subprocess.run(['python', f"{SCRIPT_DIR}/make_lookup.py"])
subprocess.run(['mv', f"{DATA_DIR}/lookup_contents.py", LOOKUP_DIR])
subprocess.run(['mv', f"{DATA_DIR}/lookup_index.py", LOOKUP_DIR])
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
ROOT_DIR = '/Users/wmodes/dev/wesbot/'
# Script directory
TRAINING_DIR = ROOT_DIR + 'training/'
# Source directory
SOURCE_DIR = TRAINING_DIR + 'source/'
# Path to the data directory
DATA_DIR = TRAINING_DIR + 'data/'
# Script to format the data
FORMAT_SCRIPT = TRAINING_DIR + 'format-data.py'
# Script to compile the data
COMPILE_SCRIPT = '/bin/cat'
# Script to split the data
SPLIT_SCRIPT = TRAINING_DIR + 'split-data.py'
# Script to check the data
CHECK_SCRIPT = TRAINING_DIR + 'check-data.py'

# extensions for training data files
SOURCE_EXT = "py"
DATA_EXT = "jsonl"

# Generate the list of files from the directory listing with the SOURCE_EXT extension
STARTING_DATA_LIST = [file_name for file_name in os.listdir(SOURCE_DIR) if file_name.endswith(f".{SOURCE_EXT}")]
# final training data file
FINAL_DATA = DATA_DIR + '/data.jsonl'

# Reformat all the data files (one at a time)
#   format-data.py email2.py email2.jsonl
print("\n# CONVERTING DATA FILES TO JSONL")
for data_file in STARTING_DATA_LIST:
    source_file = os.path.join(SOURCE_DIR, data_file)
    output_file = os.path.join(DATA_DIR, data_file.replace(f".{SOURCE_EXT}", f".{DATA_EXT}"))
    subprocess.run(['python', FORMAT_SCRIPT, source_file, output_file])

# Compile all the data files into a single file
#   cat common.jsonl discord.jsonl email.jsonl email2.jsonl > data.jsonl
print("\n# COMPILING DATA FILES INTO SINGLE FILE")
compile_command = [COMPILE_SCRIPT] + [os.path.join(DATA_DIR, data_file.replace(f".{SOURCE_EXT}", f".{DATA_EXT}")) for data_file in STARTING_DATA_LIST]
subprocess.run(compile_command, stdout=open(FINAL_DATA, 'w'))

# Split the data file into training and test sets
#   split-data.py data.jsonl 10
print("\n# SPLITTING DATA INTO TRAINING AND TEST SETS")
split_command = ['python', SPLIT_SCRIPT, FINAL_DATA, '10']
subprocess.run(split_command)

# Check the data file
#   python check-data.py data/data.jsonl
print("\n# CHECKING DATA")
check_command = ['python', CHECK_SCRIPT, FINAL_DATA]
subprocess.run(check_command)

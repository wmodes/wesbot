"""
text2jsonrecord.py - take lines on stdin and convert to json records on stdout
"""

import json
import sys

record_key = "prompts"

import sys

def create_json_from_lines():
    # Read lines from stdin
    lines = sys.stdin.readlines()

    # Remove newline characters and create an array of prompts
    prompts = [line.strip() for line in lines]

    # Print the prompts in the specified JavaScript-like format
    print(f'\nCopy this into your JSON:\n\n,\n  "{record_key}"": [')
    for prompt in prompts:
        print(f'    "{prompt}",')
    print("  ]\n")

if __name__ == "__main__":
    while True:
        create_json_from_lines()
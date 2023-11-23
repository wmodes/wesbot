"""
extract-user-prompts.py - Extracts user prompts from chatlog files    

Author: Wes Modes
Date: 2023
"""

import sys
sys.path.append('..')
import config
sys.path.append('../lookup')
import lookup_index
import re

def extract_user_prompts(log_file):
    find_words = [key.lower() for key in lookup_index.lookup_index.keys()]

    user_prompts = []

    with open(log_file, 'r') as file:
        for line in file:
            parts = line.strip().split(' - ')
            message = parts[-1]
            if message:
                try:
                    data = eval(message)
                    if data['role'] == 'user':
                        user_content = data['content'].lower()
                        # iterate through all the words in find_words
                        for word in find_words:
                            # use regular expression to find the word but
                            # only find whole words
                            pattern = r'(^|\W){}(\W|$)'.format(re.escape(word))
                            match_whole_word = re.search(pattern, user_content, re.IGNORECASE)
                            # yes, we have a match
                            if match_whole_word:
                                matching_content = data['content']
                                match_only_one_line = re.search(r'(^|[\r\n])(.*?{}.*?)([\r\n]|$)'.format(word), matching_content, re.IGNORECASE)
                                if match_only_one_line:
                                    matching_excerpt = match_only_one_line.group(2)
                                    # print(f'Found "{word}" in "{matching_excerpt}"')
                                    user_prompts.append(f"{matching_excerpt}\t{word}")
                                    break
                except:
                    pass

    # Get unique case-insensitive prompts
    unique_user_prompts = list(set(item.lower() for item in user_prompts))  # Convert to lowercase for uniqueness
    unique_user_prompts.sort()  # Sort the prompts case-insensitively

    return unique_user_prompts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract-user-prompts.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    prompts = extract_user_prompts(log_file)
    for prompt in prompts:
        print(prompt)

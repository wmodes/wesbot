import json
import re
import sys

def search_and_extract(search_string, file_path, ignore_case=False):
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            record = json.loads(line)
            
            # Extract the user and assistant messages
            user_message = next((msg['content'] for msg in record['messages'] if msg['role'] == 'user'), None)
            assistant_message = next((msg['content'] for msg in record['messages'] if msg['role'] == 'assistant'), None)

            # Check if the search string matches in either the user or assistant message using regular expression
            pattern = re.compile(search_string, re.IGNORECASE if ignore_case else 0)
            if (user_message and pattern.search(user_message)) or (assistant_message and pattern.search(assistant_message)):
                results.append(assistant_message)

    return results

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python extract.py [-i] <search_string> <file_path>")
        sys.exit(1)

    ignore_case = False
    search_string_index = 1

    if len(sys.argv) == 4 and sys.argv[1] == "-i":
        ignore_case = True
        search_string_index = 2

    search_string = sys.argv[search_string_index]
    file_path = sys.argv[search_string_index + 1]

    results = search_and_extract(search_string, file_path, ignore_case)

    if results:
        for result in results:
            print(result)
    else:
        print(f"No matches found for '{search_string}' in the user or assistant messages.")

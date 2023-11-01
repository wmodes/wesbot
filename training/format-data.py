import ast
import json
import sys

def process_input(input_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        sys.exit(1)

def extract_data_from_python(input_content):
    global input_file
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
    formatted_jsonl = ""
    for item in data:
        for message in item['messages']:
            if '```' not in message['content']:
                message['content'] = message['content'].lstrip('\n')
                message["content"] = "\n".join(line.strip() for line in message["content"].split("\n"))
                
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
    if len(sys.argv) != 3:
        print("Usage: python python2jsonl.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    python_to_jsonl(input_file, output_file)

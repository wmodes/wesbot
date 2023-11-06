import json
import sys
import os
import getch

# Check if the command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python verify-convo.py <jsonl_file>")
    sys.exit(1)

jsonl_file = sys.argv[1]

def process_jsonl_file(jsonl_file):
    records = []
    with open(jsonl_file, "r") as file:
        for line in file:
            data = json.loads(line)
            if "messages" in data:
                messages = data["messages"]
                user_content = ""
                assistant_content = ""
                for message in messages:
                    if "role" in message and "content" in message:
                        role = message["role"]
                        content = message["content"].replace("\n", "\\n")
                        if role == "user":
                            user_content = content
                        elif role == "assistant":
                            assistant_content = content
                            records.append({"user": user_content, "assistant": assistant_content})
    return records

def format_text_with_indent(text, width, indent=0):
    lines = text.splitlines()  # Split the text into lines
    padding = " " * indent  # Create the padding
    formatted_text = []
    for line in lines:
        while len(line) > width:
            # Find the last space within the specified width
            last_space = line.rfind(" ", 0, width)
            if last_space == -1:
                # If there's no space within the width, break at the width
                formatted_text.append(padding + line[:width])
                line = line[width:]
            else:
                # Break the line at the last space within the width
                formatted_text.append(padding + line[:last_space])
                line = line[last_space + 1:]
        if line:
            formatted_text.append(padding + line)
    return "\n".join(formatted_text)


def display_conversation(records):
    print("Test data processed. Press any key to advance through the conversation.")
    for record in records:
        getch.getch()  # Wait for a keypress
        # Get the terminal width
        screen_width = os.get_terminal_size().columns
        # calculate the width of the user and assistant content
        text_width = screen_width * 2 // 3
        # calculate the indent for the assistant content
        indent = screen_width - text_width
        user_content = record["user"]
        assistant_content = record["assistant"]
        user_formatted = format_text_with_indent(user_content, text_width, 0)
        assistant_formatted = format_text_with_indent(assistant_content, text_width, indent)
        print(f"\n{user_formatted}")
        # getch.getch()  # Wait for a keypress
        print(f"\n{assistant_formatted}\n")

records = process_jsonl_file(jsonl_file)
display_conversation(records)

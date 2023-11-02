"""
txt2msg.py - Take a stream of text and generate a stream of messages

Author: Wes Modes
Date: 2023
"""

import sys

template = """
  {
    "messages": [
      {
        "role": "system",
        "content": sys_combo
      }, {
        "role": "user",
        "content": "Can you tell me about?"
      }, {
        "role": "assistant",
        "content": \"\"\"{{record}}\"\"\"
      }
    ]
  },
"""

def text_to_records(text):
    # Split the input text into paragraphs based on double newline
    paragraphs = text.split('\n\n')
    
    records = []
    for i, paragraph in enumerate(paragraphs, start=1):
        # Trim leading and trailing whitespace from each paragraph
        paragraph = paragraph.strip()
        record = template.replace("{{record}}", paragraph)
        records.append(record)
    
    return records

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output_records = text_to_records(input_text)
    
    for record in output_records:
        print(record)

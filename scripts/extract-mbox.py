import argparse
import mailbox

# Define your templates
pre_text = """
[
"""

record_text = """
    {
        "messages": [
            {
                "role": "system",
                "content": "Pretend you are Wes Modes, an artist and university professor teaching new media, art, and game design. Be helpful, but not too helpful, and never obsequious. You are curious, informal, non-pedantic, compassionate, funny, ironic, and playful, but also no-nonsense and sometimes curse like a sailor. Keep replies succinct, ask curious questions, and be unafraid to admit your mistakes or say when you don't know something."
            }, {
                "role": "user",
                "content": "{{ part1 }}"
            }, {  
                "role": "assistant",
                "content": "{{ part2 }}" 
            }
        ]
    },
"""

post_text = """
]
"""

def extract_text_content(part):
    if part.get_content_type() == "text/plain":
        # Extract plain text content
        return part.get_payload(decode=True).decode('utf-8', errors='ignore')
    elif part.is_multipart():
        # Recursively process multipart content
        text_content = ""
        for subpart in part.get_payload():
            text_content += extract_text_content(subpart)
        return text_content
    else:
        # Handle other content types as needed
        return ""

def extract_part1_part2(text_content):
    part1_text = ""
    part2_text = ""
    
    lines = text_content.split('\n')
    in_part1_flag = False
    # go through each line of the text content
    for line in lines:
        # remove whitespace (including linefeeds) from the front and back of line
        line = line.strip()
        # are we at the start of part1?
        if line.startswith("> "):
            # Start of part1
            in_part1_flag = True
            line = line.lstrip("> ")
        # have we hit the end of part1?
        elif in_part1_flag and not line:
            # End of part1
            in_part1_flag = False

        # now let's build part1 and part2    
        if in_part1_flag:
            # Build part1 (including the first line)
            part1_text += line + '\n'
        else:
            # Build part2
            part2_text += line + '\n'
    
    return part1_text.strip(), part2_text.strip()

def process_message(message, processed_messages):
    subject = message.get("Subject")

    # Check if the Subject line begins with "Re:"
    if subject and subject.startswith("Re:"):
        return

    text_content = extract_text_content(message)

    # Manipulation 1: Remove lines with "Wes," "W," or "W." on their own line
    text_content = '\n'.join(line for line in text_content.split('\n') if not line.strip() in ["Wes", "W", "W."])

    # Manipulation 2: Remove lines with "Hi [person_name]," on their own line
    text_content = '\n'.join(line for line in text_content.split('\n') if not line.strip().startswith("Hi "))

    # Extract part1 and part2
    part1, part2 = extract_part1_part2(text_content)

    # Replace double linefeeds with "\n" and single linefeeds with a space
    part1 = part1.replace('\n\n', '\\n').replace('\n', ' ')
    part2 = part2.replace('\n\n', '\\n').replace('\n', ' ')

    # Escape double quotes in part1 and part2
    part1 = part1.replace('"', r'\"')
    part2 = part2.replace('"', r'\"')

    # Append the processed message to the list
    processed_messages.append((part1, part2))


# Create an empty list to store processed messages
processed_messages = []

# Create a command-line argument parser
parser = argparse.ArgumentParser(description="Extract text from mbox file with attachments and HTML emails")
parser.add_argument("mbox_file", help="Path to the mbox file")

# Parse command-line arguments
args = parser.parse_args()

# Load the mbox file specified in the command line
mbox = mailbox.mbox(args.mbox_file)

# Iterate through emails and process them
for message in mbox:
    process_message(message, processed_messages)

# Add the pre_text to the output
output = pre_text

# Iterate through processed messages and format them using record_text
for part1, part2 in processed_messages:
    message_record = record_text.replace("{{ part1 }}", part1).replace("{{ part2 }}", part2)
    output += message_record

# Add the post_text to the output
output += post_text

# Print or save the output to a file as needed
print(output)

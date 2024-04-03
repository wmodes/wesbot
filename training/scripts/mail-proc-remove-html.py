import mailbox
from bs4 import BeautifulSoup
from email.message import EmailMessage
import re
import quopri
from io import BytesIO
import csv
import sys

mbox_file_path = 'test.mbox'
output_mbox_file_path = 'test-mod.mbox'

def extract_text_from_html(html_content):
    """Extracts text from HTML content using BeautifulSoup."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def remove_html_from_message(message):
    # Process multipart/alternative specifically
    if message.get_content_type() == 'multipart/alternative':
        print("Multi-part alternative")
        text_part = None
        for part in message.get_payload():
            if part.get_content_type() == 'text/plain':
                print("Text/plain part found")
                text_part = part
                break  # Prefer text/plain part
            elif part.get_content_type() == 'text/html' and not text_part:
                print("Text/html part found")
                # Extract text from HTML only if no text/plain part is found
                text_content = extract_text_from_html(part.get_payload(decode=True))
                text_part = EmailMessage()
                text_part.set_content(text_content)
        # Replace the payload with only the text/plain part or extracted text
        if text_part:
            message.set_payload([text_part])
    elif message.is_multipart():
        # For other multipart messages, iterate and apply logic to each part
        new_parts = []
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                new_parts.append(part)
            elif part.get_content_type() == 'text/html':
                text_content = extract_text_from_html(part.get_payload(decode=True))
                new_part = EmailMessage()
                new_part.set_content(text_content)
                new_parts.append(new_part)
        if new_parts:
            message.set_payload(new_parts)
    else:
        # Handle single-part messages
        if message.get_content_type() == 'text/html':
            text_content = extract_text_from_html(message.get_payload(decode=True))
            message.set_payload(text_content)
            message.set_type('text/plain')
        elif message.get_content_type() != 'text/plain':
            return None
    return message


def message_meets_criteria(message):
    from_address = str(message.get('From', ''))  # Safely get the 'From' header as a string
    in_reply_to = message.get('In-Reply-To')
    to_address = str(message.get('To', ''))  # Safely get the 'To' header as a string
    # Check if the 'From' header contains 'wmodes@gmail.com'
    if 'wmodes@gmail.com' not in from_address:
        print("Deleting email not from 'wmodes@gmail.com'")
        return False
    # Check if the 'To' header contains 'wmodes@gmail.com'
    if 'wmodes@gmail.com' in to_address:
        print("Deleting email to 'wmodes@gmail.com'")
        return False
    # Check if the email is a reply
    if in_reply_to is None:
        print("Deleting email that is not a reply")
        return False
    return True

# Function to clean and extract text from message parts
def get_text_from_part(part):
    content_type = part.get_content_type()
    if content_type == 'text/plain':
        return part.get_payload(decode=True).decode('utf-8', errors='ignore')
    elif content_type == 'text/html':
        html_content = part.get_payload(decode=True).decode('utf-8', errors='ignore')
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()
    return ""    
    
def decode_quoted_printable(body):
    """
    Attempts to decode a quoted-printable encoded string to Unicode.
    It checks if the input is a byte string and decodes accordingly.
    """
    # Ensure the body is in bytes if it's a quoted-printable encoded string
    if isinstance(body, str):
        body = body.encode('utf-8')
    decoded_bytes = quopri.decodestring(body)
    return decoded_bytes.decode('utf-8')

def preprocess_wrapped_lines(lines):
    """
    Preprocesses wrapped lines to concatenate lines that are part of a wrapped
    "On [date] [name] wrote:" pattern into a single line, including those
    preceded with '> '.
    """
    preprocessed_lines = []
    skip_next = False
    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue
        # Check for the pattern possibly split across two lines, with or without '> '
        if i + 1 < len(lines):
            next_line = lines[i + 1].lstrip('> ').strip()
            current_line_stripped = line.lstrip('> ').strip()

            if re.match(r'^On .*$', current_line_stripped) and next_line == "wrote:":
                # Determine if we need to prepend '> ' based on the original line
                prefix = '> ' if line.startswith('> ') else ''
                # Concatenate this line with the next line, preserving '> ' if present
                concatenated_line = prefix + current_line_stripped + " " + next_line
                preprocessed_lines.append(concatenated_line)
                skip_next = True  # Flag to skip the next line since it's been concatenated
            else:
                preprocessed_lines.append(line)
        else:
            preprocessed_lines.append(line)
    return preprocessed_lines

def extract_reply_and_original(body):
    """
    Extracts the reply and the original message from a full email message body,
    considering wrapped "On [date] [name] wrote:" lines, and removes signatures.
    """
    lines = preprocess_wrapped_lines(body.splitlines())
    reply_lines = []
    original_lines = []
    original_started = False
    discard_rest = False

    for line in lines:
        if discard_rest:
            continue
        if re.match(r'^> >', line):
            discard_rest = True
        if re.match(r'^On .* wrote:$', line) and original_started:
            discard_rest = True
        elif re.match(r'^> ', line):
            original_started = True
            original_lines.append(line[2:])  # Remove leading '> '
        elif not original_started:
            reply_lines.append(line)

    # Join the lines back into text for reply and original
    reply = '\n'.join(reply_lines).strip()
    original = '\n'.join(original_lines).strip() if original_started else ""

    # strip out the pesky "On [date] [name] wrote:" lines
    reply = re.sub(r'On .* wrote:$', '', reply, flags=re.MULTILINE).strip()
    original = re.sub(r'On .* wrote:$', '', original, flags=re.MULTILINE).strip()

    # Remove signatures from both reply and original
    reply = remove_signature(reply).strip()
    original = remove_signature(original).strip()

    # Remove salutations and sign-offs from both reply and original, without signatures
    reply = clean_salutations_and_signoffs(reply).strip()
    original = clean_salutations_and_signoffs(original).strip()

    return {'original': original, 'reply': reply}

def remove_signature(text):
    """
    Removes the signature block from the text.
    The signature block is indicated by a line containing only '--'.
    """
    # Split the text into lines
    lines = text.splitlines()
    # Find the index of the line that contains only '--'
    try:
        index = lines.index('--')
        # Keep only the lines before the signature delimiter
        lines = lines[:index]
    except ValueError:
        # If '--' is not found, do nothing
        pass
    # Rejoin the lines back into a single string
    return '\n'.join(lines)

def clean_salutations_and_signoffs(text):
    # Trim whitespace at the beginning and end
    text = text.strip()

    # Remove salutations at the beginning of the text, accounting for complex names
    # This pattern looks for a greeting followed by an optional name (which may include punctuation and spaces),
    # and optionally followed by a comma, semicolon, or period. It's designed to match from the start of the string.
    salutation_pattern = r'^(hi|hello|dear)\s+[\w\s\'\.\-]*[,;.]?\s*'
    text = re.sub(salutation_pattern, '', text, flags=re.IGNORECASE | re.UNICODE)

    # Remove specific sign-offs at the end of the email, case insensitive
    # Matches the sign-offs preceded by a newline or start of the string, followed by optional whitespace.
    signoff_pattern = r'(?:\n|^)\s*(Wes|W|W\.)\s*$'
    text = re.sub(signoff_pattern, '', text, flags=re.IGNORECASE | re.UNICODE)

    text = text.strip()

    return text



def extract_data(message):
    body = ""
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() in ['text/plain', 'text/html']:
                body = get_text_from_part(part)
                break  # Assuming the first text/plain or text/html part is the main content
    else:
        body = get_text_from_part(message)
    return extract_reply_and_original(body)


def process_email():
    print("## Loading mbox")
    mbox = mailbox.mbox(mbox_file_path)
    total_messages = len(mbox)
    print(f"Total messages to process: {total_messages}")

    output_mbox = mailbox.mbox(output_mbox_file_path, create=True)
    processed_count = 0

    # Open or create a CSV file to store the extracted data
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the CSV header
        writer.writerow(['Original Message', 'Reply Message'])

        for message in mbox:
            # Skip messages marked as 'Trashed'
            if 'X-Gmail-Labels' in message and 'Trashed' in message['X-Gmail-Labels']:
                continue

            # Check if the message meets the specified criteria
            if not message_meets_criteria(message):
                continue

            modified_message = remove_html_from_message(message)
            if modified_message:
                # Extract data from the modified message
                data = extract_data(modified_message)
                # Write the extracted data to the CSV file
                writer.writerow([data['original'], data['reply']])
                output_mbox.add(modified_message)
                processed_count += 1

            print(f"\rProcessed {processed_count}/{total_messages} messages...", end='', flush=True)

    print(f"\nDone! Processed {processed_count} messages.")
    output_mbox.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mbox_file_path = sys.argv[1]
        # Derive the modified mbox file path and CSV file path
        output_mbox_file_path = mbox_file_path.rsplit('.', 1)[0] + '-mod.mbox'
        csv_file_path = mbox_file_path.rsplit('.', 1)[0] + '.csv'
    else:
        print("Usage: script.py <mbox_file_path>")
        sys.exit(1)
    process_email()
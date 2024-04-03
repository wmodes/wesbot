"""

 - Get emails from a Gmail

Author: Wes Modes
Date: 2023
"""

import sys
import os
sys.path.append(['..', './scripts'])
import google_auth as google_auth  # Import your authentication module
import config 
from googleapiclient.discovery import build
import csv

# Define folders
BASE_DIR = config.BASE_DIR  
SOURCE_FOLDER = config.SOURCE_DIR

def get_credentials():
    # Get the Google Sheets credentials
    return google_auth.get_credentials()

def list_labels(service):
    """
    List all labels in the Gmail account.
    """
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])



def main():
    # Get the Google Sheets credentials
    credentials = get_credentials()

    # Build the Gmail service
    service = build('gmail', 'v1', credentials=credentials)

    # List the Gmail labels
    list_labels(service)


if __name__ == "__main__":
    main()

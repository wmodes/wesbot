"""
google_auth.py - Authenticate for access to Google Services

Author: Wes Modes
Date: 2023
"""

import os
import sys
from google.oauth2 import service_account
sys.path.append('..')
import config   

def get_credentials():
    # Get the path to the service account JSON key file
    json_keyfile_path = config.GOOGLE_SERVICE_ACCOUNT_FILE

    # Define the scopes required for Google Sheets and Gmail
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/gmail.readonly"  # Add this line for Gmail access
    ]

    # Create a credentials object using the service account JSON key file and the defined scopes
    credentials = service_account.Credentials.from_service_account_file(
        json_keyfile_path,
        scopes=scopes
    )

    return credentials

if __name__ == "__main__":
    # Test the authentication module
    credentials = get_credentials()
    print("Authentication successful.")

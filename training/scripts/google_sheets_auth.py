"""
google_sheets_auth.py - Authenticate for access to Google Sheets

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

    # Create a credentials object using the service account JSON key file
    credentials = service_account.Credentials.from_service_account_file(
        json_keyfile_path,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    return credentials

if __name__ == "__main__":
    # Test the authentication module
    credentials = get_credentials()
    print("Authentication successful.")
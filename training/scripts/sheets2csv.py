"""

 - Get data from a Google Sheet

Author: Wes Modes
Date: 2023
"""

import google_sheets_auth as google_sheets_auth  # Import your authentication module
import sys
import os
sys.path.append('..')
import config 
from googleapiclient.discovery import build
import csv

# Define folders
BASE_DIR = config.BASE_DIR  
SOURCE_FOLDER = config.SOURCE_DIR

def get_credentials():
    # Get the Google Sheets credentials
    return google_sheets_auth.get_credentials()

def get_sheet_names(credentials, sheet_id):
    # Use the credentials and sheet ID to access the sheet
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()

    # Request to get the list of sheet properties
    spreadsheet = sheet.get(spreadsheetId=sheet_id).execute()
    sheets = spreadsheet.get('sheets', [])

    return [sheet['properties']['title'] for sheet in sheets]

def export_sheet_data_to_csv(credentials, sheet_id, sheet_name):
    # Use the credentials and sheet ID to access the sheet
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()

    # Define the range you want to read, e.g., "Sheet1!A1:C10"
    range_name = f"{sheet_name}!A1:Z1000"

    # Make the request to get values from the sheet
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        print(f'No data found in sheet: {sheet_name}')
    else:
        csv_filename = os.path.join(SOURCE_FOLDER, f'{sheet_name}.csv')
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            for row in values:
                csv_writer.writerow(row)

def main():
    # Get the Google Sheets credentials
    credentials = get_credentials()

    # Specify the Google Sheet ID from your config
    sheet_id = config.GOOGLE_SHEET_ID

    sheet_names = get_sheet_names(credentials, sheet_id)

    if not sheet_names:
        print('No sheets found in the document.')
    else:
        for sheet_name in sheet_names:
            export_sheet_data_to_csv(credentials, sheet_id, sheet_name)
            print(f'Data from sheet "{sheet_name}" exported to {SOURCE_FOLDER}/{sheet_name}.csv')

if __name__ == "__main__":
    main()

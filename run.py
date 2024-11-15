#'Pip3 freeze > requirements.txt'. to put in the dependenices into the requirements.txt file
# do not forget to validate data
import re

import gspread
from google.oauth2.service_account import Credentials

# Define the scope, which is a list of google services we are accessing
SCOPE = [ "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive" ]

#Authenticate the code to access the Company Google-spreadsheet
CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

#Open the spreadsheet
SHEET = GSPREAD_CLIENT.open('Product-Sales-Aid')




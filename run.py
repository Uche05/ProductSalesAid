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

def welcome():
    """
    Presents a simple welcome message to the user.
    """
    print("Welcome to the Product Sales Aid!")
    print("This program will help you analyze product sales data......")
    
def get_company_data():
    """
    Obtains the company basic data of company_name and country
    
    Returns:
        list: [company_name,country_of_company]
    """
    print("Enter the name of your company and country, seperated by commas\n")
    print("Like this: companyName,compnayCountry ")
    company = input("Enter the name of the company, and country: ")
    validate(company)
    company = company.split(",")
    return (company)

def update_company_data(company, worksheet):
    """
    Receives a list of company detials and
    Updates the company data in spreadsheet in needed worksheet
    Args:
        company (type: list): A list containg two values
    """
    print("Updating the spreadsheet.....")
    sheet_to_update = SHEET.worksheet(worksheet)
    sheet_to_update.append_row(company)
    print(f"{worksheet} is updating.....")
    print("Done!")

def get_sales_data(company):
    pass

def main():
    """
    Executes all program functions
    """
    company_data = get_company_data()
    update_company_data(company_data, "INFO1")
    
    
if __name__ == "__main__":
    main()
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
    while True:
        print("Enter the name of your company and country, separated by commas\n")
        print("Like this: companyName,companyCountry ")
        company = input("Enter the name of the company, and country: ")
        company = company.split(",")
        
        if validate(company):
            print("Data is valid")
            break
        
    return company

def validate(values):
    """
    Validates the input data to ensure it contains exactly two values.
    
    Args:
        values (list): List containing company name and country.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        [str(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                "Exactly 2 values required: Company and country!"
            )
    except ValueError as e:
        print(f"Error: {e}. Please try Again!!")
        return False
    return True

def update_company_data(company, worksheet):
    """
    Receives a list of company details and
    Updates the company data in spreadsheet in needed worksheet.
    
    Args:
        company (list): A list containing two values.
    """
    print("Updating the spreadsheet.....")
    sheet_to_update = SHEET.worksheet(worksheet)
    sheet_to_update.append_row(company)
    print(f"{worksheet} is updating.....")
    print("Done!")

def get_email():
    """
    Obtains the email of the company from the company_name
    
    Args:
        company (str): Name of the company.
    
    Returns:
        str: Email of the company.
    """
    company = input("Enter your company's email: ")
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, company)
        
    if emails:
        return emails[0]
    else:
        print("Your company might not receive an email of your reciept!!")
        return "No email found for the given company name"



def main():
    """
    Executes all program functions.
    """
    company_data = get_company_data()
    
    if validate(company_data):
        update_company_data(company_data, "INFO1")
    else:
        print("Try again!!!")
    
    
if __name__ == "__main__":
    main()

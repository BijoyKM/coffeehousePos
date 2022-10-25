import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coffeehousePos')


def validate_cust_name(value):
    """
    Function to validate if entered name is all characters
    """
    if value.isalpha():
        return True


def get_cust_name():
    """
    Function for getting customer name
    """
    print("*****Welcome to Coffeehouse!!*****\n")
    cust_name = input("Please enter your name:")
    if validate_cust_name(cust_name):
        print(f"Hi {cust_name}, Your order number: \n")
        print("Please provide this at the counter when paying for the order.")
    else:
        print("Please enter a valid name. Thanks")


get_cust_name()
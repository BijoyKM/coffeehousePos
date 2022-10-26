import gspread
from google.oauth2.service_account import Credentials
import random
import string

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
        if len(value) < 2 or len(value) > 25:
            return False
    return True


def create_order_num(chars=string.ascii_uppercase + string.digits, N=5):
    return ''.join(random.choice(chars) for i in range (N))


order_num = create_order_num()


def get_cust_name():
    """
    Function for getting customer name
    """
    print("*****Welcome to Coffeehouse!!*****\n")
    print("Please provide your name. It should be in between 2 to 25 characters long.")
    cust_name = input("Please enter your name: ")
    if validate_cust_name(cust_name):
        print(f"Hello {cust_name}")
        print(f"Your order number is: {order_num}")
        print("Please provide this at the counter when paying for the order.")
    else:
        print("Please enter a valid name. Thanks")


get_cust_name()

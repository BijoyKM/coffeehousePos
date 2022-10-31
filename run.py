import random
import string
from os import system, name
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
        if len(value) < 2 or len(value) > 25:
            return False
        return True


def create_order_num(chars=string.ascii_uppercase + string.digits, N=5):
    """
    Function to create alphanumeric order number of 5 character length
    """
    return ''.join(random.choice(chars) for i in range(N))


ORDER_NUM = create_order_num()
ORDER_TOTAL = None


def get_cust_name():
    """
    Function for getting customer name, 
    adds order number and customer name to order_worksheet
    """
    print("*****Welcome to Coffeehouse!!*****\n")
    while True:
        print("Please provide your name. "
              + "It should be in between 2 to 25 characters long.")
        cust_name = input("Please enter your name: ")
        if validate_cust_name(cust_name):
            print(f"Hello {cust_name}")
            order_worksheet = SHEET.worksheet("order")
            order_worksheet.update_cell(2, 1, ORDER_NUM)
            order_worksheet.update_cell(2, 2, cust_name)
            print(f"Your order number is: {ORDER_NUM}")
            print("Please provide this at the counter when paying"
                  + " for the order.")
            break
        else:
            print("Please enter a valid name. Thanks")
            
    while True:
        enter = input(f"Press Enter for Order Screen:")
        if enter == '':
            order_screen()
            break
        else:
            print(f"Please try again.")


def clear_screen():
    """
    Function to clear the terminal when switching screen
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# def update_order_total(sheetdata, order):
#     order_worksheet = SHEET.worksheet("order")
#     sheet_worksheet = SHEET.worksheet("sheetdata")
#     cell = worksheet.find("Dough")


def coffee_screen():
    """
    Function providing the coffee screen
    """
    clear_screen()
    item_price = None
    print('********************************')
    print("Coffee Screen")
    print('********************************')
    coffee_data = SHEET.worksheet('coffee').get_all_values()
    coffee_item_row = coffee_data[0]
    coffee_price_row = coffee_data[-1]
    z = 1
    for x, y in zip(coffee_item_row, coffee_price_row):
        print(f"{z}: {x} ============= € {y}\n")
        z += 1
    print("7: Payment")
    while True:
        choice = input("Enter Choice: ")
        if choice == '1':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell(2,1).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 4, item_value)
            break
            # print(f"Your order:{ORDER_NUM}:\n " + 
            # f"{item_value} {coffee_item_row[0]} Total: €{item_price}")
          

        elif choice == '2':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell(2,2).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 5, item_value)
            break
            # print(f"Your order:{ORDER_NUM}:\n " + 
            # f"{item_value} {coffee_item_row[1]} Total: €{item_price}")
    
    print(f"Your order:{ORDER_NUM}:\n " + 
            f"{item_value} {coffee_item_row[0]} Total: €{item_price}")

    sales_value_row = order_worksheet.row_values(2)
    order_worksheet.delete_rows(2)
    print(sales_value_row)
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(sales_value_row)
    

def tea_screen():
    """
    Function providing the tea screen
    """
    clear_screen()
    print('********************************')
    print("Tea Screen")
    print('********************************')
    tea_data = SHEET.worksheet('tea').get_all_values()
    print(tea_data)


def desserts_screen():
    """
    Function providing the desserts screen
    """
    clear_screen()
    print('********************************')
    print("Desserts Screen")
    print('********************************')
    desserts_data = SHEET.worksheet('desserts').get_all_values()
    print(desserts_data)


def order_screen():
    """
    Function providing the order screen
    """
    while True:
        print('********************************')
        print("Order Screen")
        print('********************************')
        print("1. Coffee")
        print("2. Tea")
        print("3. Desserts")
        print("4. Update Order")
        print("5. Checkout")
        print('********************************')
        choice = input("Enter Choice: ")
        if choice == '1':
            coffee_screen()
            break
        elif choice == '2':
            tea_screen()
            break
        elif choice == '3':
            desserts_screen()
            break
        else:
            clear_screen()
            print("Please enter a valid response like 1 for Coffee,"
                  + "2 for Tea etc.\n")


get_cust_name()
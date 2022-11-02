""" Module providing random function """
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


def create_order_num(chars=string.ascii_uppercase + string.digits, length=5):
    """
    Function to create alphanumeric order number of 5 character length
    """
    return ''.join(random.choice(chars) for i in range(length))


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
        cust_name = input("Please enter your name: \n")
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
        enter = input("Press Enter for Order Screen:\n")
        if enter == '':
            order_screen()
            break
        else:
            print("Please try again.")


def clear_screen():
    """
    Function to clear the terminal when switching screen
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def update_sales_sheet():
    """
    Function updates sales sheet with temporary order sheet
    and clears order sheet
    """
    order_worksheet = SHEET.worksheet("order")
    sales_value_row = order_worksheet.row_values(2)
    order_worksheet.delete_rows(2)
    print("Please pay at the counter. Thank you for the business.")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(sales_value_row)


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
    coffee_data = SHEET.worksheet('coffee')
    order_worksheet = SHEET.worksheet("order")
    item_num = 1
    for item_name, price in zip(coffee_item_row, coffee_price_row):
        print(f"{item_num}: {item_name} ============= € {price}\n")
        item_num += 1
    while True:
        choice = input("Enter Choice: \n")
        if choice == '1':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 1).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 4, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[0]} Total: €{item_price}")
            break
        elif choice == '2':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 2).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 5, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[1]} Total: €{item_price}")
            break
        elif choice == '3':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 3).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 6, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[2]} Total: €{item_price}")
            break
        elif choice == '4':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 4).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 7, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[3]} Total: €{item_price}")
            break
        elif choice == '5':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 5).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 8, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[4]} Total: €{item_price}")
            break
        elif choice == '6':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 6).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 9, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[5]} Total: €{item_price}")
            break

    update_sales_sheet()

    while True:
        enter = input("Press Enter to Quit.\n" +
                      "And then press Run Program to Start Again. Thanks")
        if enter == '':
            clear_screen()
            quit()
        else:
            print("Please try again.")


def tea_screen():
    """
    Function providing the tea screen
    """
    clear_screen()
    print('********************************')
    print("Tea Screen")
    print('********************************')
    tea_data = SHEET.worksheet('tea').get_all_values()
    tea_item_row = tea_data[0]
    tea_price_row = tea_data[-1]
    tea_data = SHEET.worksheet('tea')
    order_worksheet = SHEET.worksheet("order")
    item_num = 1
    for item_name, price in zip(tea_item_row, tea_price_row):
        print(f"{item_num}: {item_name} ============= € {price}\n")
        item_num += 1
    while True:
        choice = input("Enter Choice: \n")
        if choice == '1':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 1).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 10, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[0]} Total: €{item_price}")
            break
        if choice == '2':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 2).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 11, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[1]} Total: €{item_price}")
            break
        if choice == '3':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 3).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 12, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[2]} Total: €{item_price}")
            break
        if choice == '4':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 4).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 13, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[3]} Total: €{item_price}")
            break
        if choice == '5':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 5).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 14, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[4]} Total: €{item_price}")
            break
        if choice == '6':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 6).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 15, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[5]} Total: €{item_price}")
            break

    update_sales_sheet()

    while True:
        enter = input("Press Enter to Quit.\n" +
                      "And then press Run Program to Start Again. Thanks")
        if enter == '':
            clear_screen()
            quit()
        else:
            print("Please try again.")


def desserts_screen():
    """
    Function providing the desserts screen
    """
    clear_screen()
    print('********************************')
    print("Desserts Screen")
    print('********************************')
    desserts_data = SHEET.worksheet('desserts').get_all_values()
    desserts_item_row = desserts_data[0]
    desserts_price_row = desserts_data[-1]
    desserts_data = SHEET.worksheet('desserts')
    order_worksheet = SHEET.worksheet("order")
    item_num = 1
    for item_name, price in zip(desserts_item_row, desserts_price_row):
        print(f"{item_num}: {item_name} ============= € {price}\n")
        item_num += 1
    while True:
        choice = input("Enter Choice: \n")
        if choice == '1':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 1).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 16, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[0]} Total: €{item_price}")
            break
        if choice == '2':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 2).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 17, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[1]} Total: €{item_price}")
            break
        if choice == '3':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 3).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 18, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[2]} Total: €{item_price}")
            break
        if choice == '4':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 4).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 19, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[3]} Total: €{item_price}")
            break
        if choice == '5':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 5).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 20, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[4]} Total: €{item_price}")
            break
        if choice == '6':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 6).value
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            order_worksheet.update_cell(2, 21, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[5]} Total: €{item_price}")
            break
    update_sales_sheet()

    while True:
        enter = input("Press Enter to Quit.\n" +
                      "And then press Run Program to Start Again. Thanks")
        if enter == '':
            clear_screen()
            quit()
        else:
            print("Please try again.")


def get_sales():
    """
    Function to retreive sales data
    """
    sales_data = SHEET.worksheet("sales").get_all_values()
    sales_item_row = sales_data[0]
    sales_price_row = sales_data[-1]
    index_num = 1
    print("ORDER_NUM|   ITEM_NAME       |ITEM_PRICE")
    for item_name, price in zip(sales_item_row, sales_price_row):
        print(f"{index_num}| {item_name == 1} | € {price}\n")
        index_num += 1


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
        print("4. Previous Orders")
        print('********************************')
        choice = input("Enter Choice: \n")
        if choice == '1':
            coffee_screen()
            break
        elif choice == '2':
            tea_screen()
            break
        elif choice == '3':
            desserts_screen()
            break
        elif choice == '4':
            get_sales()
        else:
            clear_screen()
            print("Please enter a valid response like 1 for Coffee,"
                  + "2 for Tea etc.\n")


def main():
    """ Main function body"""
    get_cust_name()


main()

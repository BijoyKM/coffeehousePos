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

# gspreads constants
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
    Credit: https://pythonexamples.org/python-generate-random
    -string-of-specific-length/
    """
    return ''.join(random.choice(chars) for i in range(length))


# constants
ORDER_NUM = create_order_num()
ORDER_TOTAL = None


def coffee_cup_ascii():
    """Function for Coffe cup ascii art
    Credit: https://www.asciiart.eu/food-and-drinks/coffee-and-tea
    """
    print("           ) ( (")
    print("         _)__(__))")
    print("      .-'---------|")
    print("     ( C|=========|")
    print("      '-.=========|")
    print("        '_________'\n")


def tea_kettle_ascii():
    """Function for Coffe cup ascii art
    Credit: https://www.asciiart.eu/food-and-drinks/coffee-and-tea
    """
    print("                   ;,'")
    print("          _o_      ;:;'")
    print("      ,-.'---`.__ ;")
    print("     (( j`======',-'")
    print("       `(      ) ")
    print("         `-=-'    \n")


def dessert_ascii():
    """Function for Coffe cup ascii art
    Credit: https://www.asciiart.eu/food-and-drinks/coffee-and-tea
    """
    print("           o8Oo./")
    print("       ._o8o8o8Oo_.")
    print("      ._o8o8o8o8O0o_.")
    print("     (==============)")
    print("      (============)")
    print("       (----------)\n")


def get_cust_name():
    """
    Function for getting customer name,
    adds order number and customer name to order_worksheet
    """
    print("*****Welcome to Coffeehouse !!*****\n")
    print("    ******Point of Sale*****\n\n")
    coffee_cup_ascii()
    while True:
        print("Please provide your name.")
        print("It should be in between 2 to 25 characters long.\n\n")
        cust_name = input("Please enter your name: \n")
        # validates customer name
        if validate_cust_name(cust_name):
            print(f"Hello {cust_name}")
            order_worksheet = SHEET.worksheet("order")
            # update order value in order sheet
            order_worksheet.update_cell(2, 1, ORDER_NUM)
            # update customer name in order sheet
            order_worksheet.update_cell(2, 2, cust_name)
            print(f"Your order value is: {ORDER_NUM}")
            print("Please keep note of this value if you would like to search")
            print("your order details next time.")
            break
        else:
            print("Please enter a valid name. Thanks")

    while True:
        enter = input("Please type Y for Order Screen:\n")
        if enter == 'Y':
            order_screen()
            break
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
    # copies each order row values to sales sheet
    sales_value_row = order_worksheet.row_values(2)
    # clears order sheet values
    order_worksheet.delete_rows(2)
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(sales_value_row)


def pay_by_card():
    """
    function to get card digits and pin, also validates input values
    """
    # list to save card digits entered
    pay_det = []
    print("Please insert your 16 digit card number")
    while True:
        value = input("Enter Here: ")
        # validates input card number to be integer and is of 16 digits
        if value.isdigit() and len(value) == 16:
            pay_det.append(value)
            break
        else:
            print("Entered information is not valid card number")
    print(f"You have entered:{pay_det}\n")
    print("Please enter your Four digit pin.")
    while True:
        ent_value = input("Enter Here: ")
        # validates input pin to be integer and is of 4 digits
        if ent_value.isdigit() and len(ent_value) == 4:
            print("Your payment is successful.")
            break
        else:
            print("Your pin is invalid. Try again.")
    print("Thanks for the business. Please visit again.")


def coffee_screen():
    """
    Function providing the coffee screen
    """
    clear_screen()
    item_price = None
    # header
    print("        Coffee Screen")
    print('********************************')
    coffee_cup_ascii()
    # saving all values of coffee sheet to coffee_data
    coffee_data = SHEET.worksheet('coffee').get_all_values()
    # saving item row to coffee_item_row
    coffee_item_row = coffee_data[0]
    # saving price row to coffee_price_row
    coffee_price_row = coffee_data[-1]
    coffee_data = SHEET.worksheet('coffee')
    order_worksheet = SHEET.worksheet("order")
    item_num = 1
    # printing items name with their prices
    for item_name, price in zip(coffee_item_row, coffee_price_row):
        print(f"{item_num}: {item_name} ============= € {price}\n")
        item_num += 1
    print("7: Back to Order Screen")
    # depending upon user input excecutes code
    while True:
        choice = input("Enter Choice. Input number between 1 and 7: \n")
        if choice == '1':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 1).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 4, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[0]} Total: €{item_price}")
            break
        elif choice == '2':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 2).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 5, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[1]} Total: €{item_price}")
            break
        elif choice == '3':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 3).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 6, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[2]} Total: €{item_price}")
            break
        elif choice == '4':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 4).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 7, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[3]} Total: €{item_price}")
            break
        elif choice == '5':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 5).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 8, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[4]} Total: €{item_price}")
            break
        elif choice == '6':
            coffee_data = SHEET.worksheet('coffee')
            order_worksheet = SHEET.worksheet("order")
            item_price = coffee_data.cell('2', 6).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 9, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {coffee_item_row[5]} Total: €{item_price}")
            break
        elif choice == '7':
            order_screen()

    update_sales_sheet()
    pay_by_card()

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
    # header
    print("          Tea Screen")
    print('********************************')
    tea_kettle_ascii()
    # saving all values of tea sheet to tea_data
    tea_data = SHEET.worksheet('tea').get_all_values()
    # saving item row to tea_item_row
    tea_item_row = tea_data[0]
    # saving price row to tea_price_row
    tea_price_row = tea_data[-1]
    tea_data = SHEET.worksheet('tea')
    order_worksheet = SHEET.worksheet("order")
    item_num = 1
    # printing items name with their prices
    for item_name, price in zip(tea_item_row, tea_price_row):
        print(f"{item_num}: {item_name} ============= € {price}\n")
        item_num += 1
    print("7: Back to Order Screen")
    # depending upon user input excecutes code
    while True:
        choice = input("Enter Choice. Input number between 1 and 7: \n")
        if choice == '1':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 1).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 10, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[0]} Total: €{item_price}")
            break
        if choice == '2':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 2).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 11, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[1]} Total: €{item_price}")
            break
        if choice == '3':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 3).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 12, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[2]} Total: €{item_price}")
            break
        if choice == '4':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 4).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 13, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[3]} Total: €{item_price}")
            break
        if choice == '5':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 5).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 14, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[4]} Total: €{item_price}")
            break
        if choice == '6':
            tea_data = SHEET.worksheet('tea')
            order_worksheet = SHEET.worksheet("order")
            item_price = tea_data.cell('2', 6).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 15, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {tea_item_row[5]} Total: €{item_price}")
            break
        if choice == '7':
            order_screen()

    update_sales_sheet()
    pay_by_card()

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
    # header
    print("       Desserts Screen")
    print('********************************')
    dessert_ascii()
    # saving all values of tea sheet to desserts_data
    desserts_data = SHEET.worksheet('desserts').get_all_values()
    # saving item row to desserts_item_row
    desserts_item_row = desserts_data[0]
    # saving price row to desserts_price_row
    desserts_price_row = desserts_data[-1]
    desserts_data = SHEET.worksheet('desserts')
    order_worksheet = SHEET.worksheet("order")
    item_num = 1
    # printing items name with their prices
    for item_name, price in zip(desserts_item_row, desserts_price_row):
        print(f"{item_num}: {item_name} ============= € {price}\n")
        item_num += 1
    print("7: Back to Order Screen")
    # depending upon user input excecutes code
    while True:
        choice = input("Enter Choice. Input number between 1 and 7: \n")
        if choice == '1':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 1).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 16, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[0]} Total: €{item_price}")
            break
        if choice == '2':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 2).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 17, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[1]} Total: €{item_price}")
            break
        if choice == '3':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 3).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 18, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[2]} Total: €{item_price}")
            break
        if choice == '4':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 4).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 19, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[3]} Total: €{item_price}")
            break
        if choice == '5':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 5).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 20, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[4]} Total: €{item_price}")
            break
        if choice == '6':
            desserts_data = SHEET.worksheet('desserts')
            order_worksheet = SHEET.worksheet("order")
            item_price = desserts_data.cell('2', 6).value
            # updating order sheet item price cell with chosen item price
            order_worksheet.update_cell(2, 3, item_price)
            item_value = 1
            # updating order sheet item name with value 1
            order_worksheet.update_cell(2, 21, item_value)
            print(f"Your order#: {ORDER_NUM}")
            print(f"{item_value} {desserts_item_row[5]} Total: €{item_price}")
            break
        if choice == '7':
            order_screen()
    update_sales_sheet()
    pay_by_card()

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
    sales_data = SHEET.worksheet("sales")
    input_order_num = input("Please enter your order value in UPPERCASE: ")
    # saving ORDER_NUM column data of sales sheet to a list
    order_value_list = sales_data.col_values(1)
    # deleting ORDER_NUM value from the list
    del order_value_list[0]
    # finding if entered order value is in sales sheet
    # this returns None if entered order value is not in sales sheet
    # if order value is there then returns row and colume of that cell
    order_num_cell = sales_data.find(input_order_num)
    if order_num_cell is None:
        print(f"{input_order_num} is not a Valid order value"
              + " as no purchases are registered against it yet.")
    # checks if entered order value is not in ORDER_NUM column in sales sheet
    if input_order_num not in order_value_list:
        print(f"{input_order_num} is not a Valid order value"
              + " as no purchases are registered against it yet.")
    else:
        # saves row number
        row_num = order_num_cell.row
        # gets customer name column
        cust_col = (order_num_cell).col + 1
        # gets customer value from cell
        customer = sales_data.cell(row_num, cust_col).value
        # gets order price column
        order_val_col = cust_col + 1
        # gets order price value from cell
        order_val = sales_data.cell(row_num, order_val_col).value
        # gets headings row from sales sheet
        name_row = sales_data.row_values(1)
        # gets order details row from sales sheet
        item_row = sales_data.row_values(row_num)
        # list to store headings from sales sheet
        name_list = []
        # loop to find if order details row cell and heading row cell have data
        # order detail cell will have item_value set to 1
        for col_name, col_num in zip(name_row, item_row):
            if col_name and col_num:
                last_item = col_name
                name_list.append(last_item)
        print("Your search details are:\n")
        print(f"ORDER VALUE: {input_order_num}")
        print(f"Customer Name : {customer}")
        # third item on name_list will heading which has item_value set to 1
        print(f"Order : {name_list[3]}")
        print(f"Price: €{order_val}")
        print('********************************')
        print("Please Enter Your Choice.")
        print('********************************')


def order_screen():
    """
    Function providing the order screen
    """
    while True:
        # header
        print('********************************')
        print("Order Screen")
        print('********************************')
        print("1. Coffee")
        print("2. Tea")
        print("3. Desserts")
        print("4. Search Your Old Order")
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
                  + " 2 for Tea etc.\n")


def main():
    """ Main function body"""
    get_cust_name()


main()

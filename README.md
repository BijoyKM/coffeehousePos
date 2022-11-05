# CoffeehousePOS

## Overview
### This is an interactive self service, Point of Sale solution that uses Google Sheets API.The program enables user to order coffee/tea/desserts. This also imitate a cashless experience for the user as he/she will pay by card. The Order information is stored which can be retrived by entering valid order value.
The project should run in a CLI, deployed via Heroku, using Python.

*** This is a fictional python project for educational purposes only ***


![CoffeehousePOS](/assets/images/readmeimages/WelcomeScreen.jpg "Welcome screen image")

## Live site can be viewed here. 
# [Coffeehousepos](https://coffeehousepos.herokuapp.com/)

## Repository
## [https://github.com/BijoyKM/coffeehousePos](https://github.com/BijoyKM/coffeehousePos)



# Index – Table of Contents
- [User Experience (UX)](#user-experience-ux)
- [Features](#features)
- [Technologies Used](#tecnologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)


# User Experience (UX)
## User Stories
* ## As a User I want to be able to:
1. The program provides clear and concise information about the coffeehouse, the items, their prices.
2. Easily navigate between the different functions available in the program.
3. Access the product and order database implemented via Google Sheets through the CoffeehousePos application.
4. To create a application which can take order with minimal steps and complexities like self service kiosk operated by the customer only.
5. User can traverse through different items screens to view avaliable items with their prices.

# 1. Strategy
* The main purpose creating this application is to create a python project which will explore the basic implementation of a self serving cashless kiosk used by customer entirely.

# 2. Scope
* Easy to navigate options and functions which user will find very simple and straightforward.
* User can navigate the items and their prices with user input validated properly.
* User can retrieve his / her order depending on valid order value entered.

# 3. Structure
The flowchart of the application can be found ![here](/assets/images/readmeimages/CoffeehouseposFlowChart.jpg).


## The program is a command line program that leads the user through series of questions.
* The program starts by getting the customer name input.

* The program validates the entered customer name and generates an order value. This order value can be used to retrieve order details later.
* The generated order value and customer name is entered in the coffeehousePos spreadsheet under sheet name order. 

* Then the program leads to the Order screen of the program. This screen has four options.
   * First option leads to the Coffee screen.
   * Second option leads to the Tea screen.
   * Third option leads to the Desserts screen.
   * Fourth option leads to the Order search option
   * User input is validated, wrong entry brings back the user to order screen to choose right option
   
* Coffee screen provides 7 options including list of various coffees and their prices.
   * Option 1 to 6 provide user to choose between different coffee items.
   * Option 7 help user to go back to order screen just in case if user has changed mind.
   * User input is validated, wrong entry prompts user to input the correct choice.
   * If user choose option one to 6, program will show the order item selected with price. The order value is also shown.
   * The order sheet is populated with item price. Also item number 1 is assigned to the item selected by the customer for the same row.
   * This order sheet row is then copied to sales sheet to mark as transaction as final.
   * Then the order sheet row is cleared to be used for the next order.
   * The program then requests the 16 digit card number of the customer which is validated for integer and number of digits which is 16 in this case.
   * The program then requests the 4 digit pin of the customer which is validated for integer and number of digits which is 4 in this case.
   * After successful payment the program thanks the customer for the business and provides option to exit the program by pressing Enter.

* Tea screen provides 7 options including list of various teas and their prices.
   * Option 1 to 6 provide user to choose between different tea items.
   * Option 7 help user to go back to order screen just in case if user has changed mind.
   * User input is validated, wrong entry prompts user to input the correct choice.
   * If user choose option one to 6, program will show the order item selected with price. The order value is also shown.
   * The order sheet is populated with item price. Also item number 1 is assigned to the item selected by the customer for the same row.
   * This order sheet row is then copied to sales sheet to mark as transaction as final.
   * Then the order sheet row is cleared to be used for the next order.
   * The program then requests the 16 digit card number of the customer which is validated for integer and number of digits which is 16 in this case.
   * The program then requests the 4 digit pin of the customer which is validated for integer and number of digits which is 4 in this case.
   * After successful payment the program thanks the customer for the business and provides option to exit the program by pressing Enter.

* Desserts screen provides 7 options including list of various desserts and their prices.
   * Option 1 to 6 provide user to choose between different dessert items.
   * Option 7 help user to go back to order screen just in case if user has changed mind.
   * User input is validated, wrong entry prompts user to input the correct choice.
   * If user choose option one to 6, program will show the order item selected with price. The order value is also shown.
   * The order sheet is populated with item price. Also item number 1 is assigned to the item selected by the customer for the same row.
   * This order sheet row is then copied to sales sheet to mark as transaction as final.
   * Then the order sheet row is cleared to be used for the next order.
   * The program then requests the 16 digit card number of the customer which is validated for integer and number of digits which is 16 in this case.
   * The program then requests the 4 digit pin of the customer which is validated for integer and number of digits which is 4 in this case.
   * After successful payment the program thanks the customer for the business and provides option to exit the program by pressing Enter.

* Fourth option on Order screen provides user a search feature which looks up Order value entered by user to see if it matches an previous order.
  * This order value entered by the user is searched in the whole sales sheet and then in column heading of ORDER_NUM.
  * If the value is not found the user is informed that the value entered is not an order value yet. And further directed to the order screen to complete order or enter the correct order value.
  * If the value is found then the corresponding order value details like customer name, item sold and price are displayed. And further directed to the order screen to complete order.


# 4. Skeleton
## Wireframes
 * There were no wireframes created for this project. As the application stays in same Terminal of 80 characters wide and 24 rows high. The content changes but the window remains the same.

# 5. Surface
* ## Color
  * Due to the nature of project no external colour is used.

* ## Font
  * No extenal fonts are used in this project.


# Features
## Existing Features
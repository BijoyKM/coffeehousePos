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

### Welcome Screen

![Welcome screen image](/assets/images/readmeimages/WelcomeScreenmore.jpg "Welcome screen image")
  * When the program starts we have the Welcome Screen. This has a Coffee House Point of Sale header. 
  * It has an a simple but nice coffee ascii art image representing the Coffeehouse business.
  * This screen also asks and let user to enter his/her name. The name is validated for string to have atleast 2 and maximum 25 characters.
  * Once a valid user name is entered, an order value is generated. User is prompted to take note of this value just in case to search for details later.
  * The generated order value and customer name is stored in Google sheets coffeehouse, under order sheet for the cycle of the order. Once order is complete order sheet row is appended to sales sheet. Then order sheet row is cleared for next order use.
  ![ordersheetimage](/assets/images/readmeimages/ordersheetimage.jpg "ordersheetimage")
  * The user is then prompted to press Y, in order to go to Order screen.
  * The get_cust_name() function is used for this screen.

  ![get_cust_name()image](/assets/images/readmeimages/get_cust_name_func.jpg "get_cust_name()image")

  * The validate_cust_name() and creat_order_num() function are also used for this screen.

  ![validate_cust_name() and creat_order_num() image](/assets/images/readmeimages/welcomescreenfuncimages.jpg "validate_cust_name() and creat_order_num() image")


### Order Screen

![Order screen image](/assets/images/readmeimages/orderscreenimage.jpg "Order screen image")
 * When the user enters Y and after validation, he /she is lead to the Order screen.
 * To keep the interface simple to use and uncluttered the menu divides the functionality into 4 options : 
    * 1) Coffee Screen 
    * 2) Tea Screen
    * 3) Desserts Screen
    * 4) Search Your Old Order
* The order_screen() function is used for this screen.

  ![order_screen()image](/assets/images/readmeimages/order_screen_func_image.jpg "order_screen()image")

* The get_sales() function is also used in order screen to get sales for Search Your Old Order option.

  ![get_sales()image](/assets/images/readmeimages/get_sales_func_image.jpg "get_sales()image")


* The clear_screen() function is also used in order screen to clear screen in the end.

  ![clear_screen()image](/assets/images/readmeimages/clear_screen_func_image.jpg "clear_screen()")

### Coffee Screen

![Coffee screen image](/assets/images/readmeimages/coffeescreenimage.jpg "Coffee screen image")
* Coffee screen provides 7 options with a sublist of various coffees and their prices.
   * It has a header Coffee Screen and coffee ascii art image.
   * Option 1 to 6 provide user to choose between different coffee items.
   * Option 7 help user to go back to order screen just in case if user has changed mind.
   * User input is validated, wrong entry prompts user to input the correct choice.
   * If user choose option one to 6, program will show the order item selected with price. The order value is also shown.
   * The order sheet is populated with item price. Also item number 1 is assigned to the item selected by the customer for the same row.
   * This order sheet row is then copied to sales sheet to mark as transaction as final.
   ![Sales sheet image](/assets/images/readmeimages/salessheetimage.jpg "Sales sheet image")
   * Then the order sheet row is cleared to be used for the next order.
   * The program then requests the 16 digit card number of the customer which is validated for integer and number of digits which is 16 in this case.
   * The program then requests the 4 digit pin of the customer which is validated for integer and number of digits which is 4 in this case.
   * After successful payment the program thanks the customer for the business and provides option to exit the program by pressing Enter.

   ![order_payment_image](/assets/images/readmeimages/order_payment_screen_image.jpg "order_payment_image")

   * coffee_screen(), update_sales_sheet() and pay_by_card() functions are used in Coffee screen.

![coffee_screen()image](/assets/images/readmeimages/coffee_screen_func_image.jpg "coffee_screen()image")
![update_sales_sheet()image](/assets/images/readmeimages/updatesalesfunc_image.jpg "update_sales_sheet()image")
![pay_by_card()image](/assets/images/readmeimages/paybycardfunc_image.jpg "pay_by_card()image")



### Tea Screen

![Tea screen image](/assets/images/readmeimages/Teascreenimage.jpg "Tea screen image")
* Tea screen also work in similar fashion as Coffee screen.
* It has a header for Tea screen  and tea ascii art image.
* Option 1 to 6 provide user to choose between different tea items.
* Option 7 help user to go back to order screen just in case if user has changed mind.
* User input is validated, wrong entry prompts user to input the correct choice.
* If user choose option one to 6, program will show the order item selected with price. The order value is also shown.
* The order sheet is populated with item price. Also item number 1 is assigned to the item selected by the customer for the same row.
* This order sheet row is then copied to sales sheet to mark as transaction as final.
![Sales sheet image](/assets/images/readmeimages/salessheetimage.jpg "Sales sheet image")
* Then the order sheet row is cleared to be used for the next order.
* The program then requests the 16 digit card number of the customer which is validated for integer and number of digits which is 16 in this case.
* The program then requests the 4 digit pin of the customer which is validated for integer and number of digits which is 4 in this case.
* After successful payment the program thanks the customer for the business and provides option to exit the program by pressing Enter.
* Tea_screen(), update_sales_sheet() and pay_by_card() functions are used in Tea screen.



### Desserts Screen

![Desserts screen image](/assets/images/readmeimages/dessertsscreenimage.jpg "Desserts screen image")
* Desserts screen also work in similar fashion as Coffee and Tea screen.
* It has a header for Desserts screen  and desserts ascii art image.
* Option 1 to 6 provide user to choose between different dessert items.
* Option 7 help user to go back to order screen just in case if user has changed mind.
* User input is validated, wrong entry prompts user to input the correct choice.
* If user choose option one to 6, program will show the order item selected with price. The order value is also shown.
* The order sheet is populated with item price. Also item number 1 is assigned to the item selected by the customer for the same row.
* This order sheet row is then copied to sales sheet to mark as transaction as final.
![Sales sheet image](/assets/images/readmeimages/salessheetimage.jpg "Sales sheet image")
* Then the order sheet row is cleared to be used for the next order.
* The program then requests the 16 digit card number of the customer which is validated for integer and number of digits which is 16 in this case.
* The program then requests the 4 digit pin of the customer which is validated for integer and number of digits which is 4 in this case.
* After successful payment the program thanks the customer for the business and provides option to exit the program by pressing Enter.
* Desserts_screen(), update_sales_sheet() and pay_by_card() functions are used in Desserts screen.


### Search Your Old Order


![Order search image](/assets/images/readmeimages/ordersearchscreenimage.jpg "Order search image")
* When option 4 is pressed, the user can enter a previous order value to search the details.
* The value can be 5 character long alphanumeric string and has to be in uppercase.
* This order value entered by the user is searched in the whole sales sheet and then in column heading of ORDER_NUM.
* If the value is not found the user is informed that the value entered is not an order value yet. And further directed to the order screen to complete order or enter the correct order value.

![Invalid entry search image](/assets/images/readmeimages/invalidordersearchimage.jpg "Invalid entry search image")

* If the value is found then the corresponding order value details like customer name, item sold and price are displayed. And further directed to the order screen to complete order.


### User prompts and messages
* If user enter invalid character for name input following message will display.

![Invalid name image](/assets/images/readmeimages/invalidnamemessage.jpg "Invalid name image")

* If user enter invalid character for Y input on Welcome screen following message will display.

![Invalid Y image](/assets/images/readmeimages/invalidYinputimage.jpg "Invalid Y image")

* If user enter invalid item number on any items screen following message will display.

![Invalid Item input image](/assets/images/readmeimages/invaliditeminputimage.jpg "Invalid Item input image")

* If user enter invalid card number on any items payment screen following message will display.

![Invalid card paymentinputimage](/assets/images/readmeimages/invalidcardinputimage.jpg "Invalid card paymentinputimage")

* If user enter invalid pin number on any items payment screen following message will display.

![Invalid pin inputimage](/assets/images/readmeimages/invalidpininputimage.jpg "Invalid pin inputimage")


## Future Features which can implemented
* To use HTML and CSS to give user a more attractive UI.
* To add functions to get more order details in one go. 
* To add functions where user can buy more items in one go.
* To add functions where user can see the basket with items to be paid for.


# Technologies Used
*  ## Languages Used
    * [Python](https://www.python.org/) 

* ## Frameworks, Libraries & Programs Used
    * [Google Sheets](https://en.wikipedia.org/wiki/Google_Sheets) : used as the external database to store item names, prices, order and sales information
    * [Google Drive API](https://developers.google.com/drive/api/v3/about-sdk) : used to generate      credentials used in the project to securely access the Google Spreadsheet.
    * [Google Sheets API](https://developers.google.com/sheets/api) : used to support interactions (e.g. 
      read/write functionality) between the code and data stored in the Google Spreadsheet.
    * [gspread](https://docs.gspread.org/en/latest/) : Python API for Google Sheets
    * [Google Auth](https://google-auth.readthedocs.io/en/master/) : Google authentication library for  
      Python required to use the credentials generated for Google Drive API
    * [Git](https://git-scm.com/) : was used for version control by utilising the Gitpod terminal to commit 
      to Git and Push to GitHub.
    * [Github](https://github.com/) : is used as the respository for the projects code after being pushed 
      from Git.
    * [Heroku](https://heroku.com/) : is used to deploy the application and provides an enviroment in which the code can execute.
    * [draw.io](https://app.diagrams.net/) : is used to create the flow chart.


# Testing

## Manual Testing 
   
![Manual Testing](/assets/images/readmeimages/ManualTestImage.jpg "Manual Testing")

* PEP8 Testing:
  Since Pep8online is down, so installed So as a alternative option have installed a extension within VS Code to flag any errors.

   * Run the command pip3 install pycodestyle Note that this extension may already be installed, in which case this command will do nothing.
   * In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
   * Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.
   * Select pycodestyle from the list.
   * PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

Any styling errors would show up as a warning or critical error.
In the image below I have highlighted a red rectangle around the results. Left to right you have critical errors, warnings and info. We do not have to worry about the info flags. 
  * There are 0 Critical errors and 3 warnings which are not related to coffeehousepos code.

![pccodesytlecheck](/assets/images/readmeimages/pycodestylecheck.jpg "pccodesytlecheck")

## Bugs

* During earlier stage in program the Order value search were producing wrong order details. This was due the user entered value was searched in the whole sales Google sheet. 
Hence if user entered username as order value or item name as value the search was producing errors.

![error order search](/assets/images/readmeimages/errordersearch.jpg "error order search")

* To fix this a list was created with all values of ORDER_NUM column. And from that list ORDER_NUM was removed as it was not real order value created but an heading in the sheet. User entered order value was ran through this list as well which fixed the issue.
* There are no other bugs detected.

## Known Bugs

![knownbug search](/assets/images/readmeimages/knownbug.jpg "knownbug search")

* Since order value search is going through two if statements sometime if the order value is not found we get 2 errors instead of one.

![iffunctionssearch](/assets/images/readmeimages/knownbug.jpg "iffunctionssearch")


## Deployment

The site was deployed to Heroku. Please follow the below steps.

### Deployment steps

1. add the list of requirements by writing in the terminal "pip3 freeze > requirements.txt"
2. Add six and colorama==0.4.4 as they didn't seem to add automatically
2. Git add and git commit the changes made
3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen
5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

The page of your project opens.
8. Choose "settings" from the menu on the top of the page
9. Go to section "Config Vars" and click button "Reveal Config Vars"

10. Go to git pod and copy the content of "creds.json" file
11. In the field for "KEY" enter "CREDS" - all capital letters
12. Paste the content of "creds.json" and paste to field "VALUE" Click button "Add"
13. Add another key "PORT" and value "8000"

14. Go to section "Build packs" and click "Add build pack"
    - in this new window - click Python and "Save changes"
    - click "Add build pack" again
    - in this new window - click Node.js and "Save changes"
    - take care to have those apps in this order: Python first, Node.js second, drag and drop if needed

15. Next go to "Deploy" in the menu bar on the top 
16. Go to section "deployment method", choose "GitHub"
17. New section will appear "Connect to GitHub" - Search for the repository to connect to
18. type the name of your repository and click "search"
19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"
21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy
22. Click "Deploy branch" Once the program runs:
you should see the message "the app was sussesfully deployed"
23. Click the button "View"

### Forking the GitHub repository
By forking out of this repository you will be able to view and edit the code without affecting the original repository. 

1. Locate the GitHub repository. Link can be found [here](https://github.com/BijoyKM/coffeehousePos).
2. Click the button in the top right-hand corner "Fork"
3. This will take you to your own repository to a fork that is called the same as the original branch. 

### Making a local clone

1. Locate the GitHub repository. Link can be found [here](https://github.com/BijoyKM/coffeehousePos).
2. Next to the green Gitpod button you will see a button "code" with an arrow pointing down
3. You are given the option to open with GitHub desktop or download zip
4. You can also copy https full link, go to git bash and write git clone and paste the full link

### Google spreadsheet and APIs
  * Google sheets was used as database.
  * There were 5 sheets created. Coffee, Tea, Desserts, Order and Sales
  * Coffee sheet had following headings and values.

  ![Coffee sheet image](/assets/images/readmeimages/coffeeitemsheetimage.jpg "Coffee sheet image")
  

  * Tea sheet had following headings and values.

  ![Tea sheet image](/assets/images/readmeimages/teaitemsheetimage.jpg "Tea sheet image")


  * Desserts sheet had following headings and values.

  ![Desserts sheet image](/assets/images/readmeimages/dessertsitemsheetimage.jpg "Desserts sheet image")

  ### Set up APIs using the Google Cloud Platform

     * Access the [Google Cloud Platform](https://console.cloud.google.com/)
     * Create a new project and give it a unique name, then select the project to go to the project dashboard
     * Setup Google Drive credentials 

        * Click on the hamburger menu in the top left of the screen to access the navigation menu
        * On the left hand menu select 'APIs and Services' and then 'Library'
        * Search for Google Drive API
        * Select Google Drive API and click on 'enable' to get to the API and Services Overview page 
        * Click on the Create Credentials button near the top left of the screen
        * Select 'Google Drive' API from the dropdown for 'Credential Type'
        * Select the 'Application Data' radio button in the 'What data will you be accessing' area
        * Select the 'No, I'm not using them' for the 'Are you planning to use this API with Compute 
          Engine, Kubernetes Engine, App Engine, or Cloud Functions?' area
        * Cick Next
        * On the Create Service Account page, step 1 is to enter a service account name in the first 
          text box.  Any value can be entered here.
        * Click on 'Create and Continue'
        * On step 2, 'Grant this service account access to project',  select Basic -> Editor from  
          the 'Select a Role' dropdown.
        * Click on Continue
        * On step 3, 'Grant users access to this service account', simply press Done, no input is 
          necessary
        * On the next page, click on the service account name created (listed under the Service 
          Accounts area) to go to the configuration page for the new service account.
        * Click on the KEYS tab at the top middle of the screen.
        * Click on the Add Key dropdown and select Create New Key.
        * Select the JSON radio button then click Create. The json file with the new API credentials 
          will download your machine. 
        * Rename the downloaded file to creds.json.  This filename is already listed in the   project .  gitignore file and so no further action will be needed to prevent it being  accidentally uploaded to github 
        * Copy the new creds.json file into the local clone
        * In the creds.json file, copy the value for "client email" and then on Google Drive, share 
          the spreadsheet created above with this email address assigning a role of Editor.


### Enable Google Sheets API 
* Go back to the dashboard for the project on Google Cloud Platform and access the navigation menu as before
    * On the left hand menu select 'APIs and Services' and then 'Library'
    * Search for Google Sheets API
    * Select Google Sheets API and click on 'enable'

  * Install gspread and google-auth libraries in the development environment using the command 'pip3 install gspread google-auth'


# Acknowledgments

I would like to thank and acknowledge the following people:
* My Mentor Rahul Lakhanpal for all his feedback, guidance and support for this project.
* My daughter and Wife who helped with the testing the application patiently.
* Code Institute, Kasia and Kenan for their helpful advice during the weekly stand-up meetings.
* Slack Community and also MSLETB A and B group students.






































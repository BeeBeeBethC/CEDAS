import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from prettytable import PrettyTable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('CEDAS')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data) commented out as working(row 1)

def display_menu():
    print("Welcome to S-DAS, The Stock-Data Automation System.\n")
    print("Please select: \n")
    print("Press '1' to run the application\n")
    print("Press '2' for Instructions\n")
    print("Press '3' to Exit\n")

def handle_menu_choice(choice):
    if choice == "1":
        print("Option 1 selected. Application Running\n")
        run_application()
    elif choice == "2":
        print("Option 2 selected. Please wait for instructions to show.\n")
        how_to_use()
    elif choice == "3":
        print("Option 3 selected.\n")
        print("Thank you for Using S-DAS\n")
        print("Exiting program now.")
    else:
        print("Invalid choice. Please press a Number '1' '2' or '3'.\n")
        print("Alternatively Press '2' to review Instructions.\n")

def fetch_headers():
    """
    retrieves Headers (flavours) from the spreadsheet and displays. 
    for loop now added in to loop over each flavour and requesting 
    user input for quantity sold and asking users to confirm is 
    correct. 
    """
    worksheet = SHEET.worksheet('sales')
    headers = worksheet.row_values(1)
    header_input_dict = {}
    for header in headers:
        value = input(f"Please enter the value for '{header}': \n")
        header_input_dict[header] = value
    print("DEBUG: headers fetched:", header_input_dict)
    
def handle_dictionary_input(headers):
    collected_data = []
    for header in headers:
        print(f"DEBUG: processing header '{header}'")
        value = input(f"Enter value for '{header}': ")
        collected_data[header] = value
    return collected_data

def confirm_data(collected_data):
    print("\nHere are the values you've entered:")
    for key, value in collected_data:
        print(f"{key}: {value}")
    is_correct = input("\nConfirm your data (Y/N): ")
    if is_correct == "Y":
        update_worksheet(collected_data, worksheet)
    elif is_correct == "N":
        print("Please review your data and enter it again")
    else:
        print("Invalid choice. please press Y or N on your keyboard to proceed")

def update_worksheet(collected_data, worksheet):
    print(f"updating {worksheet} worksheet... \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(collected_data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_figures(sales_row):
    """
    compare sales figures with stock figures. 
    the zip method used with a for loop allows us to run through
    and iterate two lists simultaneously.
    """
    print("Calculating Surplus Figures...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_figures = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_figures.append(surplus)
    
    return surplus_figures

def get_last_5_figures_sales():
    """ 
    collects columns of figures and collects last 5 entries 
    for each cheesecake and returns this data as a list of lists
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 8):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns

def calculate_stock_figures(figures):
    """
    calculates average stock figures generating dynamic
    stock order recommendations
    """
    print("Calculating Stock Figures Please Wait...\n")
    new_stock_figures = []
    
    for column in figures:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_figures.append(round(stock_num))

    return new_stock_figures

def order_new_stock():
    """
    Displays stock to order in the terminal ready for the next day.
    using the enumerate function, it takes the collection of data 
    and returns it in a paired list for example {'Lemon': '7'}
    """
    print("Retrieving stock to order...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    headers = stock[0]
    last_row = stock[-1]
    To_order = {}

    for i, header in enumerate(headers):
        To_order[header] = last_row[i]

    print(To_order)

def run_application():
    """
    when option 1 is selected from the menu, it runs all 
    other functions before looping back round and 
    displays menu until user chooses option 3.
    """
    fetch_headers()
    #handle_dictionary_input('headers')
    #confirm_data('collected_data')
    #update_worksheet(collected_data, "sales")
    #new_surplus_figures = calculate_surplus_figures(sales_figures)
    #update_worksheet(new_surplus_figures, "surplus")
    #sales_columns = get_last_5_figures_sales()
    #stock_figures = calculate_stock_figures(sales_columns)
    #update_worksheet(stock_figures, "stock")
    #order_new_stock()

def how_to_use():
    """
    Instructions on how to use S-DAS
    add to as functions multiply!
    """
    print("Select function from menu options using numbers 1-3, press Enter.\n")
    print("Option 1, Type in sales figures to corresponding cheesecake flavours, press Enter\n")
    print("Allow the programme run all the functions shown in the terminal it will return you to the main menu once complete.\n")
    print("Option 2, Takes you to instructions on how to use S-DAS (You are currently here.)\n")
    print("Option 3, Exits the program\n")

def main():
    """
    Runs an indefinite loop displaying and handling the users choice
    breaks out of loop if user selects option '3'
    """
    while True:
        display_menu()
        choice = input("Select your Option: \n")
        handle_menu_choice(choice)
        if choice == "3":
            break

if __name__ == "__main__":
    main()
import gspread
from google.oauth2.service_account import Credentials
from datetime import date, timedelta, datetime
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


def display_menu():
    # shows what options are available to users
    print("\nWelcome to CEDAS")
    print("The Cheesecake Emporium Data Automation System.")
    print("\nPlease select: \n")
    print("Press '1' to run the application\n")
    print("Press '2' for Instructions\n")
    print("Press '3' display data from a specific date.")
    print("(Pressing '3' also provides all data in a table if date\
           entered is before 2024-08-01)\n")
    print("Press '4' to fetch stock data.\n")
    print("Press '5' to Exit.\n")


def handle_menu_choice(choice):
    # handles user choice
    if choice == "1":
        print("\nOption 1 selected.")
        print("---------------------------------------------------")
        print("Application Running")
        run_application()
    elif choice == "2":
        print("Option 2 selected.")
        print("---------------------------------------------------")
        print("Please wait for instructions to show.")
        how_to_use()
    elif choice == "3":
        print("Option 3 selected.")
        print("---------------------------------------------------")
        fetch_data_from_user_input()
    elif choice == "4":
        print("Option 4 selected.")
        print("---------------------------------------------------")
        fetch_stock_data()
    elif choice == "5":
        print("Option 5 selected.")
        print("---------------------------------------------------")
        print("Thank you for Using CEDAS\n")
        print("Exiting program now.")
    else:
        print("\nInvalid choice. Press a Number '1' '2' '3' '4' or '5'.\n")
        print("\nAlternatively Press '2' to review Instructions.\n")


def fetch_stock_data():
    """
    Retrieves and prints all data from the "stock" worksheet.
    """
    stock_worksheet = SHEET.worksheet("stock")
    stock_data = stock_worksheet.get_all_values()
    
    table = PrettyTable()
    table.field_names = stock_data[0]  # Assuming the first row is the header
    
    for row in stock_data[1:]:
        table.add_row(row)
    
    print(table)


def add_date_to_data(headers):
    default_start_date = datetime(2024, 8, 1)
    sales = SHEET.worksheet("sales")
    data = sales.get_all_values()
    
    last_date_str = None
    for row in reversed(data):
        if row[0]:
            try:
                last_date = datetime.strptime(row[0], "%Y-%m-%d")
                last_date_str = row[0]
                break
            except ValueError:
                print(f"Skipping invalid date format: {row[0]}")
                continue

    if last_date_str:
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
        next_date = last_date + timedelta(days=1)
    else:
        next_date = default_start_date
    print("DEBUG: LAST DATE:", last_date_str)
    print("DEBUG: NEXT DATE TO BE ADDED:", next_date.strftime("%Y-%m-%d"))
    
    user_values = user_input_flavours(headers)
    new_row = [next_date.strftime("%Y-%m-%d")] + user_values
    print("DEBUG: NEW ROW TO BE ADDED:", new_row)

    return new_row


def fetch_data_from_date(date_str):
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    sales_data = SHEET.worksheet("sales").get_all_values()
    filtered_data = [sales_data[0]]
    for row in sales_data[1:]:
        row_date = datetime.strptime(row[0], "%Y-%m-%d")
        if row_date >= target_date:
            filtered_data.append(row)
    return filtered_data


def fetch_data_from_user_input():
    while True:
        date_str = input("Please enter the date (YYYY-MM-DD): \n")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            filtered_data = fetch_data_from_date(date_str)
            table = PrettyTable()
            table.field_names = filtered_data[0]
            for row in filtered_data[1:]:
                table.add_row(row)
            print(table)
            break
        except ValueError:
            print("Invalid date. please write as YYYY-MM-DD.")
            print("Please try again. \n")


def fetch_headers():
    # Retrieves headers from the spreadsheet.
    worksheet = SHEET.worksheet('sales')
    headers = worksheet.row_values(1)[1:]
    print("DEBUG: Headers Fetched:", headers)
    return headers


def user_input_flavours(headers):
    """
    while loops added to headers for loop to check for input validation
    nested while loop added. refuses to move forward until the
    correct data value is given.
    """
    while True:
        headers_fetched = {}
        for header in headers:
            while True:
                # ----- try, except statement from W3Schools -----
                try:
                    value = input(f"\nPlease enter a value between 0 and 20:\
                                   for '{header}'  \n")
                    value = int(value)
                    if 0 <= value <= 20:
                        print("Value valid. Proceed.")
                        headers_fetched[header] = value
                        break
                    else:
                        print("Invalid input, Enter a number between 0 and 20")
                except ValueError:
                    print(f"'{value}' is not valid. Please try again.")
        return list(headers_fetched.values())

"""
some functions below are inspired by the love sandwiches walkthrough
unless otherwise stated within the following code. 
"""
def update_worksheet(new_row, worksheet):
    # updates multiple worksheets
    print(f"\nUpdating {worksheet} worksheet... \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(new_row)
    print(f"{worksheet} worksheet updated successfully\n")


def get_last_5_figures_sales():
    # Collects columns of figures and last 5 entries. Returns a list of lists.
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 8):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns


def calculate_stock_figures(input_lists):
    """
    Calculates average figures, provides stock recommendations.
    isinstance reviewed from W3Schools
    use of Replit for debug see "TESTING.md" for more information.
    """ 
    print("Calculating Stock Figures Please Wait...\n")
    new_stock_figures = []
    for column in input_lists:
        int_column = [int(num) for num in column
                      if isinstance(num, str) and num.isdigit()]
        if int_column:
            average = sum(int_column) / len(int_column)
            stock_num = average * 1.1
            new_stock_figures.append(round(stock_num))
        else:
            new_stock_figures.append(0)

    return new_stock_figures


def order_new_stock(new_stock_figures):
    """
    Retrieves data and displays stock to order
    in a table.
    table from PrettyTable. 
    knowledge gained from PrettyTable official
    documentation.
    """
    
    print("Retrieving stock to order...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    headers = stock[0]
    to_order = {}

    for i, header in enumerate(headers):
        if i < len(new_stock_figures):
            to_order[header] = new_stock_figures[i]
        else:
            to_order[header] = 0
    print("Stock to order:")
    table = PrettyTable()
    table.field_names = ["Item", "Stock to Order"]
    for item, stock in to_order.items():
        table.add_row([item, stock])

    print(table)


def run_application():
    """
    function layout taken from Love Sandwiches.
    (main function call in Love Sandwiches)
    function changed to ensure smooth application
    running from developing the main menu
    display function.
    Runs all functions, loops and displays 
    menu until option 4 selected.
    """
    headers = fetch_headers()
    new_row = add_date_to_data(headers)
    update_worksheet(new_row, "sales")
    sales_columns = get_last_5_figures_sales()
    new_stock_figures = calculate_stock_figures(sales_columns)
    update_worksheet(new_stock_figures, "stock")
    order_new_stock(new_stock_figures)


def how_to_use():
    # Instructions, how to use S-DAS
    print("---------------------------------------------------")
    print("Select function from menu options using numbers 1-4")
    print("Press Enter.")
    print("---------------------------------------------------")
    print("Option 1, Type in latest sales figures")
    print("CEDAS asks for values correspoding to cheesecake flavours")
    print("Allow the application to run until the menu options show")
    print("---------------------------------------------------")
    print("Option 2, Takes you to instructions on how to use CEDAS")
    print("---------------------------------------------------")
    print("Option 3, Users can fetch data from a set date.")
    print("NOTE: CEDAS returns values after 01-08-2024 only")
    print("Enter a date from 01-08-2024 in format YYYY-MM-DD")
    print("Option 4 retrieves all stock data")
    print("---------------------------------------------------")
    print("Option 5 Exits the programme.")
    print("NOTE: CEDAS asks for values until option 5 is selected")


def main():
    # Runs infinite loop, handles choice, breaks loop if option 4 selected.
    while True:
        display_menu()
        choice = input("\nSelect your Option: \n")
        handle_menu_choice(choice)
        if choice == "5":
            break


if __name__ == "__main__":
    main()

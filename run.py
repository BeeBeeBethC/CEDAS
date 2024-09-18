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

def display_menu():
    #shows what options are available to users
    print("\nWelcome to S-DAS, The Stock-Data Automation System.\n")
    print("\nPlease select: \n")
    print("Press '1' to run the application\n")
    print("Press '2' for Instructions\n")
    print("Press '3' to get data using a specific date.\n")
    print("Press '4' to Exit.\n")

def handle_menu_choice(choice):
    #handles user choice
    if choice == "1":
        print("\nOption 1 selected.\n")
        print("---------------------------------------------------")
        print("Application Running\n")
        run_application()
    elif choice == "2":
        print("\nOption 2 selected.\n")
        print("---------------------------------------------------")
        print("Please wait for instructions to show.\n")
        how_to_use()
    elif choice == "3":
        print("\nOption 3 selected.\n")
        print("---------------------------------------------------")
        #fetch_data_from_user_input()
    elif choice =="4":
        print("\nOption 4 selected.\n")
        print("---------------------------------------------------")
        print("Thank you for Using S-DAS\n")
        print("Exiting program now.")
    else:
        print("\nInvalid choice. Please press a Number '1' '2' '3' or '4'.\n")
        print("\nAlternatively Press '2' to review Instructions.\n")

def add_date_to_data():
    start_date = datetime.date(2024, 9, 1)
    print(f"DEBUG: ", (start_date))
    data = SHEET.worksheet("sales").get_all_values()
    date_header = ["Date"]
    updated_data = [date_header + data[0]]
    current_date = start_date
    for row in data[1:]:
        updated_row = [current_date] + data[row_index]
        updated_data.append(updated_row)
        current_date += datetime.timedelta(days=1)
    sales.clear()
    sales.update("A1", updated_data)
    print("DEBUG: Date successfully added to column 1!")

def fetch_data_from_date(date_str):
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    sales_data = SHEET.worksheet("sales").get_all_values()
    filtered_data = [data for data in sales_data if datetime.strptime(data['date'],"%Y-%m-%d") >= target_date]
    
    return filtered_data

def fetch_data_from_user_input():
    while True:
        date_str = input("Please enter the date (YYYY-MM-DD): \n")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            filtered_data = fetch_data_from_date(date_str)
            print(filtered_data)
            break
        except ValueError:
            print("Invalid date. please write as YYYY-MM-DD. please try again. \n")

def fetch_headers():
    #gets headers from the spreadsheet and displays.
    worksheet = SHEET.worksheet('sales')
    headers = worksheet.row_values(1)
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
                value = input(f"\nPlease enter the value for '{header}': \n")
                try:
                    value = int(value)
                    print("valid")
                    headers_fetched[header] = value
                    break
                except ValueError:
                    print(f"'{value}' is not a number. try again")

        return list(headers_fetched.values())

def update_worksheet(input_list, worksheet):
    #updates multiple worksheets
    print(f"\nUpdating {worksheet} worksheet... \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(input_list)
    print(f"{worksheet} worksheet updated successfully\n")

def get_last_5_figures_sales():
    # Collects columns of figures. Collects last 5 entries. Returns data as a list of lists.
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 8):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns

def calculate_stock_figures(input_lists):
    # Calculates average figures, provides stock recommendations.
    print("Calculating Stock Figures Please Wait...\n")
    new_stock_figures = []
    
    for column in input_lists:
        int_column = [int(num) for num in column if isinstance(num, str) and num.isdigit()]
        
        if int_column:
            average = sum(int_column) / len(int_column)
            stock_num = average * 1.1
            new_stock_figures.append(round(stock_num))
        else:
            new_stock_figures.append(0)

    return new_stock_figures

def order_new_stock(new_stock_figures):
    # Retrieves data and displays stock to order in a table.
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
    # Option 1 selected, runs all other functions, loops and displays menu until option 3 selected.
    #add_date_to_data()
    headers = fetch_headers()
    input_list = user_input_flavours(headers)
    update_worksheet(input_list, "sales")
    sales_columns = get_last_5_figures_sales()
    new_stock_figures = calculate_stock_figures(sales_columns)
    update_worksheet(new_stock_figures, "stock")
    order_new_stock(new_stock_figures)

def how_to_use():
    # Instructions, how to use S-DAS
    print("---------------------------------------------------")
    print("\nSelect function from menu options using numbers 1-3, press Enter.\n")
    print("---------------------------------------------------")
    print("\nOption 1, Type in sales figures to corresponding cheesecake flavours, press Enter\n")
    print("Allow the programme run all the functions shown in the terminal it will return you to the main menu once complete.\n")
    print("---------------------------------------------------")
    print("\nOption 2, Takes you to instructions on how to use S-DAS (You are currently here.)\n")
    print("---------------------------------------------------")
    print("\nOption 3, Exits the program\n")
    print("---------------------------------------------------")

def main():
    # Runs indefinite loop, handles choice, breaks if option 3 selected.
    while True:
        display_menu()
        choice = input("\nSelect your Option: \n")
        handle_menu_choice(choice)
        if choice == "4":
            break

if __name__ == "__main__":
    main()
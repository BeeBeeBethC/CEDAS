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
SHEET = GSPREAD_CLIENT.open('CEDAS')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data) commented out as working

def get_sales_figures():
    """ 
    gets sales figures from user input
    function logic: get_sales_figures runs a while loop to 
    check for any user input error. This includes not enough 
    numerical values, text instead of numerical values, too
    too many numerical values (for this data 
    set to be valid, it is seven numerical values that are 
    required for input) 
    """
    while True:
        print("Please enter most recent sales figures.")
        print("Data input should consist of seven numbers separated by commas.")
        print("Example data: 1,2,3,4,5,6,7\n")

        figure_str = input("Enter your sales figures here: \n") 

        figures = figure_str.split(',')
    
        if validate_figures(figures):
            print("FIGURES PROVIDED ARE VALID!")
            break
    return figures

def validate_figures(values):
    """
    inside the try, converts the string values from the data
    input into integers.
    Raises ValueError if the string cannot be converted into
    integers or if there arent enough data values. 
    when using CEDAS is 7 values exactly.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values are required. You provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid Data: {e}, please try again.\n")
        return False

    return True

def update_sales_worksheet(figures):
    """
    update Sales Worksheet by adding a new row of data using the
    figures provided. 
    """
    # feedback provided in terminal.
    print("Updating Figures to corresponding worksheet...\n")
    figures_worksheet = SHEET.worksheet("sales")
    figures_worksheet.append_row(figures)
    print("Figures Updated Successfully!\n")

def update_surplus_worksheet(figures):
    """
    update Surplus Worksheet by adding a new row of data using the
    figures provided. 
    """
    # feedback provided in terminal.
    print("Updating Figures to corresponding worksheet...\n")
    figures_worksheet = SHEET.worksheet("surplus")
    figures_worksheet.append_row(figures)
    print("Surplus Figures Updated Successfully!\n")

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

def main():
    """
    Runs all functions declared
    """
    figures = get_sales_figures()
    sales_figures = [int(num) for num in figures]
    update_sales_worksheet(sales_figures)
    new_surplus_figures = calculate_surplus_figures(sales_figures)
    update_surplus_worksheet(new_surplus_figures)

print("Welcome to CEDAS, The Cheesecake Emporium Data Automation System.\n")
main()
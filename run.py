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

        sales_figures = figure_str.split(',')
    
        if validate_figures(sales_figures):
            print("DATA PROVIDED IS VALID!")
            break
    return sales_figures

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


get_sales_figures()
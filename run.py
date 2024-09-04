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
    function logic: get_sales_figures runs a while loop until 
    the correct amount of values are fed in. (for this data 
    set it is 7 numerical values that are required for data 
    to be valid) 
    """

    print("Please enter most recent sales figures.")
    print("Data input should consist of seven numbers separated by commas.")
    print("Example data: 1,2,3,4,5,6,7\n")

    figure_str = input("Enter your sales figures here: \n")
    print(f"The Data Provided is as follows: {figure_str}\n")

get_sales_figures()
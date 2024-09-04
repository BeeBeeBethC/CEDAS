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
# while True:
    print("Please enter most recent sales figures.")
    print("Data input should consist of seven numbers separated by commas.")
    print("Example data: 1,2,3,4,5,6,7\n")

    figure_str = input("Enter your sales figures here: \n") 

    sales_figures = figure_str.split(',')
    print(sales_figures)

    # if validate_data(sales_figures):
       #  print("DATA PROVIDED IS VALID!")
       #  break
#return sales_figures

get_sales_figures()
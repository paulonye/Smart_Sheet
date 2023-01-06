from main import capture_data
from sheet_connect import get_connect_sheet
import pandas as pd
import os

#This scrapes the data from Yahoo Finance
data = capture_data()

#This imports the service account credentials that will allow us access the sheet
client = get_connect_sheet()

#Once the connection has been made, the Google Sheet can now be accessed
push_sheet = client.open('test_sheet')

#data_sheet = push_sheet.worksheet('data')

#data_df = pd.DataFrame.from_dict(push_sheet.worksheet('data').get_all_records())

def append_new_data(df, sheet_name):
    """This function takes in the dataframe and the name of the sheet you wish
    to append the data to """

    values = df.values.tolist()
    push_sheet.values_append(sheet_name, {'valueInputOption': 'USER_ENTERED'},
                             {'values': values})

print(data)

try:
    append_new_data(data,'data')
except Exception as e:
    print('Could not append')
    print(e)
    os._exit(0)



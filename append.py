from main import capture_data
from sheet_connect import get_connect_sheet
import pandas as pd
import send_mail
import os


#This scrapes the data from Yahoo Finance
try:
    data = capture_data()
except Exception as e:
    send_mail.send_email(e)
    os._exit(0)

#This imports the service account credentials that will allow us access the sheet
try:
    client = get_connect_sheet()
#Once the connection has been made, the Google Sheet can now be accessed
    push_sheet = client.open('test_sheet')
except Exception as e:
    send_mail.send_email(e)
    os._exit(0)


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
    send_email(e)
    os._exit(0)



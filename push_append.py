import os

try:
    import send_mail
    from main import capture_data
    from sheet_connect import get_connect_sheet
    from sheet_connect import push_to_sheets
    from sheet_connect import append_new_data
    import pandas as pd
except Exception as e:
    send_mail.send_email(e)
    os._exit(0)

#EXTRACTION AND TRANSFORMATION PHASE
#This scrapes the data from Yahoo Finance
try:
    data = capture_data()
except Exception as e:
    send_mail.send_email(e)
    os._exit(0)

#LOADING PHASE
try:
    #This imports the service account credentials that will allow us access the sheet
    client = get_connect_sheet()
    #Once the connection has been made, the Google Sheet can now be accessed
    push_sheet = client.open('test_sheet')
    #opening the data sheet
    data_push = push_sheet.worksheet('data2')
    data_push_df = pd.DataFrame.from_dict(data_push.get_all_records())
except Exception as e:
    send_mail.send_email(e)
    os._exit(0)

print(data)

#You can either load or append the data
try:
    if len(data_push_df) == 0:
        push_to_sheets(data_push, data)
    else:
        append_new_data(data,'data2','test_sheet')
except Exception as e:
    print('Could not append')
    send_mail.send_email(e)
    os._exit(0)



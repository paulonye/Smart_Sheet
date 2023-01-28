import mail
from scrape import capture_data
from connect import get_connect_sheet, push_to_sheets, append_new_data
import pandas as pd

#EXTRACTION AND TRANSFORMATION PHASE
#This scrapes the data from Yahoo Finance

def batch_records(data, sheet_name, worksheet):

    df = pd.read_csv(data)

    client = get_connect_sheet()

    push_sheet = client.open(sheet_name)

    data_push = push_sheet.worksheet(worksheet)

    data_push_df = pd.DataFrame.from_dict(data_push.get_all_records())

    if len(data_push_df) == 0:
        push_to_sheets(data_push, df)
    else:
        append_new_data(df, worksheet, sheet_name)



from main import capture_data
from sheet_connect import get_connect_sheet
from sheet_connect import push_to_sheets
import pandas as pd

#This scrapes the data from Yahoo Finance
data = capture_data()

#This imports the service account credentials that will allow us access the sheet
client = get_connect_sheet()

#This makes a connection to the Google Sheet
push_sheet = client.open('test_sheet')

#We then need to access the particular worksheet we want to work with
#You can use push_sheet.worksheets() to print out all worksheets present 
#in the Google Worksheet
data_push = push_sheet.worksheet('data')

#Using the function we imported from sheet_connect, we can then push
#the scraped data to the Google sheet
push_to_sheets(data_push, data)


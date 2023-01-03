from main import capture_data
from sheet_connect import get_connect_sheet
from sheet_connect import push_to_sheets
import pandas as pd

data = capture_data()

client = get_connect_sheet()

push_sheet = client.open('test_sheet')

data_push = push_sheet.worksheet('data')

push_to_sheets(data_push, data)


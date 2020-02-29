import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC


GDriveJSON = 'class-line-bot-269706-ecbdc72edd1e.json'
GSpreadSheet = 'BotData'

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
key = SAC.from_json_keyfile_name(GDriveJSON, scope)
gc = gspread.authorize(key)
worksheet = gc.open(GSpreadSheet).sheet1

def add_homework_value(text):
    data = worksheet.col_values(1)
    index = 1
    for cell in data:
        index+=1

    worksheet.update_acell('A'+str(index),text)

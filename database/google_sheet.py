import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

class google_sheet():

    def __init__(self):
        GDriveJSON = 'database/class-line-bot-269706-ecbdc72edd1e.json'
        GSpreadSheet = 'BotData'

        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        self.worksheet = gc.open(GSpreadSheet).sheet1

    def find_data_len(self, row):
        data = self.worksheet.col_values(row)
        len = 0
        for cell in data:
            len += 1
        return len

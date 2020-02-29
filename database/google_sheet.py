import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC


GDriveJSON = 'database/class-line-bot-269706-ecbdc72edd1e.json'
GSpreadSheet = 'BotData'

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
key = SAC.from_json_keyfile_name(GDriveJSON, scope)
gc = gspread.authorize(key)
worksheet = gc.open(GSpreadSheet).sheet1

def add_homework_value(text):
    index = find_data_len(1)+1
    worksheet.update_acell(f'A{index}',text)

def print_homework_value():
    list = worksheet.col_values(1)

    index = 0
    data = ''
    for cell in list:
        if index != 0:
            data += f'{index}. {cell}\n'
        index += 1
    return data

def remove_homework_value(index=1):
    len = find_data_len(1)

    index+=1
    value = worksheet.acell(f'A{index}').value
    while index <= len:
        val = worksheet.acell(f'A{index+1}').value
        worksheet.update_acell(f'A{index}',val)
        index += 1
    return value

def remove_all_homework_value():
    len = find_data_len(1)
    index = 0
    while index <= len:
        if index != 0:
            worksheet.update_acell(f'A{index+1}','')
        index += 1

def add_transClass_value(Clist):
    index = find_data_len(4)+1
    worksheet.update_acell(f'D{index}',Clist[0])
    worksheet.update_acell(f'E{index}',Clist[1])
    worksheet.update_acell(f'F{index}',Clist[2])
    worksheet.update_acell(f'G{index}',Clist[3])

def print_transClass_value():
    day1 = worksheet.col_values(4)
    class1 = worksheet.col_values(5)
    day2 = worksheet.col_values(6)
    class2 = worksheet.col_values(7)

    index = 0
    data = ''
    for cell in day1:
        if index != 0:
            data += f'{index}. {day1[index]} {class1[index]}與{day2[index]} {class2[index]} 調課\n'
        index += 1
    return data

def remove_all_transClass_value():
    len = find_data_len(4)
    index = 0
    while index <= len:
        if index != 0:
            worksheet.update_acell(f'D{index+1}','')
            worksheet.update_acell(f'E{index+1}','')
            worksheet.update_acell(f'F{index+1}','')
            worksheet.update_acell(f'G{index+1}','')
        index += 1



def find_data_len(row):
    data = worksheet.col_values(row)
    len = 0
    for cell in data:
        len += 1
    return len

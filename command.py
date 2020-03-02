import json
from os import remove
from datetime import datetime
from database.google_sheet import google_sheet

sheet = google_sheet()

def help():
    with open("database/command.txt", mode='r', encoding="utf-8") as file:
        data = file.read()
    return data


## 課堂
def today():
    now = datetime.now()
    todayOfWeek = datetime.now().weekday()+1
    if now.hour+8 >= 24:
        if todayOfWeek == 7:
            todayOfWeek = 1
        else:
            todayOfWeek += 1

    reply = f'{now.month}/{now.day} {(now.hour+8)%24}:{now.minute}'
    if todayOfWeek == 6 or todayOfWeek == 7:
        reply += '[今天沒有上課]'
    else:
        with open("database/curriculum.json", mode='r', encoding="utf-8") as file:
            data = json.load(file)
        lesson = '\n'
        for i in range(1,9):
            lesson = lesson+ str(i)+' '+ data[str(todayOfWeek)][str(i)]+'\n'
        reply += lesson
    return reply


def next_lesson():
    todayOfWeek = datetime.now().weekday()+1
    now = datetime.now()
    hour = now.hour+8
    nextLesson = hour-6 if hour<13 else hour-7

    if todayOfWeek == 6 or todayOfWeek == 7:
        reply = '[今天沒有上課]'
    else:
        if nextLesson > 8 or nextLesson < 1:
            reply = '[沒有課了]'
        else:
            with open("database/curriculum.json", mode='r', encoding="utf-8") as file:
                data = json.load(file)
            reply = data[str(todayOfWeek)][str(nextLesson)]
    return reply

## 作業
def add_homework(homework):
    index = sheet.find_data_len(1)+1
    sheet.worksheet.update_acell(f'A{index}',homework)
    return f'[{homework}已加入作業]'

def print_homework():
    list = sheet.worksheet.col_values(1)

    index = 0
    data = ''
    for cell in list:
        if index != 0:
            data += f'{index}. {cell}\n'
        index += 1
    return f'```\n{data}```'

def remove_homework(homework):
    index = int(homework)
    len = sheet.find_data_len(1)+1

    index+=1
    reply = sheet.worksheet.acell(f'A{index}').value
    while index < len:
        val = sheet.worksheet.acell(f'A{index+1}').value
        sheet.worksheet.update_acell(f'A{index}',val)
        index += 1
    return f'[{reply}已移除]'

def remove_all_homework():
    len = sheet.find_data_len(1)+1
    index = 0
    while index < len:
        if index != 0:
            sheet.worksheet.update_acell(f'A{index+1}','')
        index += 1
    return f'[作業已清空]'


##調課
def add_transClass(CL):
    Clist = CL.split(' ',3)
    index = sheet.find_data_len(4)+1
    sheet.worksheet.update_acell(f'D{index}',Clist[0])
    sheet.worksheet.update_acell(f'E{index}',Clist[1])
    sheet.worksheet.update_acell(f'F{index}',Clist[2])
    sheet.worksheet.update_acell(f'G{index}',Clist[3])
    return f'[{CL} 已加入]'

def print_transClass():
    day1 = sheet.worksheet.col_values(4)
    class1 = sheet.worksheet.col_values(5)
    day2 = sheet.worksheet.col_values(6)
    class2 = sheet.worksheet.col_values(7)

    index = 0
    data = ''
    for cell in day1:
        if index != 0:
            data += f'{index}. {day1[index]} {class1[index]}與{day2[index]} {class2[index]} 調課\n'
        index += 1

    reply = data
    return f'```\n{reply}```'

def remove_all_transClass():
    len = sheet.find_data_len(4)+1
    index = 0
    while index < len:
        if index != 0:
            sheet.worksheet.update_acell(f'D{index+1}','')
            sheet.worksheet.update_acell(f'E{index+1}','')
            sheet.worksheet.update_acell(f'F{index+1}','')
            sheet.worksheet.update_acell(f'G{index+1}','')
        index += 1
    return '[調課已清空]'

##考試
def add_test(T):
    Tlist = T.split(' ',1)
    index = sheet.find_data_len(2)+1
    sheet.worksheet.update_acell(f'B{index}',Tlist[0])
    sheet.worksheet.update_acell(f'C{index}',Tlist[1])
    return f'[{T} 已加入]'

def print_test():
    day = sheet.worksheet.col_values(2)
    test = sheet.worksheet.col_values(3)

    index = 0
    data = ''
    for cell in day:
        if index != 0:
            data += f'{index}. {day[index]} {test[index]}\n'
        index += 1

    reply = f'```\n{data}```'
    return reply

def remove_test(test):
    index = int(test)
    len = sheet.find_data_len(1)+1

    index+=1
    reply = sheet.worksheet.acell(f'B{index}').value + ' ' + sheet.worksheet.acell(f'C{index}').value
    while index < len:
        val = sheet.worksheet.acell(f'B{index+1}').value
        sheet.worksheet.update_acell(f'B{index}',val)
        val = sheet.worksheet.acell(f'C{index+1}').value
        sheet.worksheet.update_acell(f'C{index}',val)
        index += 1
    return f'[{reply}已移除]'

def remove_all_test():
    len = sheet.find_data_len(2)+1
    index = 0
    while index < len:
        if index != 0:
            sheet.worksheet.update_acell(f'B{index+1}','')
            sheet.worksheet.update_acell(f'C{index+1}','')
        index += 1
    return '[調課已清空]'

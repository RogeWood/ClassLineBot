import json
from os import remove
from datetime import datetime
import database.google_sheet as google_sheet

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
    google_sheet.add_homework_value(homework)
    return f'[{homework}已加入作業]'

def print_homework():
    data = google_sheet.print_homework_value()
    return f'```\n{data}```'

def remove_homework(homework):
    reply = google_sheet.remove_homework_value(int(homework))
    return f'[{reply}已移除]'

def remove_all_homework():
    reply = google_sheet.remove_all_homework_value()
    return f'[作業已清空]'


##調課
def add_transClass(CL):
    List = CL.split(' ',3)
    google_sheet.add_transClass_value(List)

    return f'[{CL} 已加入]'

def print_transClass():
    reply = google_sheet.print_transClass_value()
    return f'```\n{reply}```'

def remove_all_transClass():
    google_sheet.remove_all_transClass_value()
    return '[調課已清空]'

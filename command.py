import json
from os import remove
from datetime import datetime

def help():
    with open("command.txt", mode='r', encoding="utf-8") as file:
        data = file.read()

    return data


## 課堂
def today_lesson():
    now = datetime.now()
    todayOfWeek = datetime.now().weekday()+1
    if now.hour+8 > 24:
        if todayOfWeek == 7:
            todayOfWeek = 1
        else:
            todayOfWeek += 1

    reply = ""
    if todayOfWeek == 6 or todayOfWeek == 7:
        reply = '[今天沒有上課]'
    else:
        with open("curriculum.json", mode='r', encoding="utf-8") as file:
            data = json.load(file)
        lesson = '\n'
        for i in range(1,9):
            lesson = lesson+ str(i)+' '+ data[str(todayOfWeek)][str(i)]+'\n'
        reply = lesson

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
            with open("curriculum.json", mode='r', encoding="utf-8") as file:
                data = json.load(file)
            reply = data[str(todayOfWeek)][str(nextLesson)]

    return '['+reply+']'


## 作業
def add_homework(homework):
    with open("homework.txt", mode='a', encoding="utf-8") as file:
        file.write('\n'+homework)

    return '[作業已增加]'


def print_homework():
    with open("homework.txt", mode='r', encoding="utf-8") as file:
        data = file.read()

    return data


def remove_homework():
    data = ''
    with open("homework.txt", mode='r', encoding="utf-8") as file:
        n=0
        for line in file:
            n +=1
            if n == 1:
                reply = line
            else:
                data += line

    with open("homework.txt", mode='w', encoding="utf-8") as file:
        file.write(data)

    return '['+reply+'已移除]'

def remove_all_homework():
    remove("homework.txt")
    return '[已清空]'

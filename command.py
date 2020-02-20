import json
from datetime import datetime

def help():
    with open("command.txt", mode='r', encoding="utf-8") as file:
        data = file.read()

    return data


def today_lesson():
    todayOfWeek = datetime.now().weekday()+1
    reply = "\n"
    if todayOfWeek == 6 or todayOfWeek == 7:
        reply = '今天沒有上課'
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
    nextLesson = now.hour-6 if now.hour<13 else now.hour-7

    if todayOfWeek == 6 or todayOfWeek == 7:
        reply = '今天沒有上課'
    else:
        if nextLesson > 8:
            reply = '沒有課了'
        else:
            with open("curriculum.json", mode='r', encoding="utf-8") as file:
                data = json.load(file)
            reply = data[str(todayOfWeek)][str(nextLesson)]

    return reply

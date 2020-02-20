import json
from datetime import datetime

def help():
    with open("command.txt", mode='r', encoding="utf-8") as file:
        data = file.read()
    return data

def today_lesson():
    todayOfWeek = datetime.now().weekday()+1
    ans = "\n"
    if todayOfWeek == 6 or todayOfWeek == 7:
        ans = '今天沒有上課'
    else:
        with open("curriculum.json", mode='r', encoding="utf-8") as file:
            data = json.load(file)
        lesson = '\n'
        for i in range(1,9):
            lesson = lesson+ str(i)+' '+ data[str(todayOfWeek)][str(i)]+'\n'
        ans = lesson
    return ans

import json
from os import remove
from datetime import datetime

def help():
    with open("command.txt", mode='r', encoding="utf-8") as file:
        data = file.read()

    return data


## 課堂
def today():
    now = datetime.now()
    todayOfWeek = datetime.now().weekday()+1
    if now.hour+8 > 24:
        if todayOfWeek == 7:
            todayOfWeek = 1
        else:
            todayOfWeek += 1

    reply = f'{now.month}/{now.day} {(now.hour+8)%24}:{now.minute}'
    if todayOfWeek == 6 or todayOfWeek == 7:
        reply += '[今天沒有上課]'
    else:
        with open("curriculum.json", mode='r', encoding="utf-8") as file:
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
            with open("curriculum.json", mode='r', encoding="utf-8") as file:
                data = json.load(file)
            reply = data[str(todayOfWeek)][str(nextLesson)]

    return reply


## 作業
def add_homework(homework):
    with open("homework.txt", mode='a', encoding="utf-8") as file:
        file.write(homework+'\n')

    return f'[{homework}已加入作業]'


def print_homework():
    with open("homework.txt", mode='r', encoding="utf-8") as file:
        data = file.read()

    return f'```\n{data}```'

def remove_homework(homework):
    data = ''
    finded = False
    with open("homework.txt", mode='r', encoding="utf-8") as file:
        n=0
        for line in file:
            n += 1
            if n == int(homework):
                finded = True
                reply = line
            else:
                data += line

    if finded:
        with open("homework.txt", mode='w', encoding="utf-8") as file:
            file.write(data)
        return f'[{reply}已移除]'
    else:
        return '[沒有此作業]'

def remove_all_homework():
    remove("homework.txt")
    return '[作業已清空]'


##調課
def add_transClass(CL):
    #12/13 化學 1/13 國文
    List = CL.split(' ',3)
    data = {List[0]: List[1], List[2]: List[3]}

    with open("transClass.json",mode='r', encoding="utf-8") as file:
        get = json.load(file)

    get.update(data)

    with open("transClass.json",mode='w', encoding="utf-8") as file:
        json.dump(get,file)

    return f'[{CL} 已加入]'

def print_transClass():

    with open("transClass.json",mode='r', encoding="utf-8") as file:
        data = json.load(file)

    l = True
    line = 0
    reply = ''
    for key, value in data.items():
        line+=1
        if line<3:
            continue
        if l == True:
            reply += f'{key} {value} 與 '
            l = False
        else:
            reply += f'{key} {value} 調課\n'
            l = True

    return reply

def remove_all_transClass():
    remove("transClass.json")
    data = {"test": "test", "Test": "test"}
    with open("transClass.json",mode='w', encoding="utf-8") as file:
        json.dump(data, file)
    return '[調課已清空]'

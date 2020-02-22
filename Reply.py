import command

def reply_Text_Message(text):

    if text == "Hi" or text == "hi":
        reply = 'Hello'

    elif text == "今天課表":
        reply = command.today_lesson()

    elif text == "help":
        reply = command.help()

    elif text == "下節課" or text == "next":
        reply = command.next_lesson()

    elif text == "time":
        time = datetime.now()
        reply = str(time.hour+8) + ':'+str(time.minute)

    elif "hw" in text:
        if 'rm' in text:
            HW = text[6:]
            if text == "hw rm all":
                reply = command.remove_all_homework()
            elif HW == ' ' or HW == '':
                reply = command.remove_homework('1')
            else:
                reply = command.remove_homework(HW)

        elif "add" in text:
            HW = text[7:]
            if HW == '' or HW == ' ':
                reply = '未輸入作業\n[bot hw add (作業)]'
            else:
                reply = command.add_homework(HW)
        elif text == "hw" or text == "hw ":
            reply = command.print_homework()

    else:
        reply = '未知指令\n[bot help可查詢指令]'

    return reply

import command

def reply_Text_Message(text):

    if text == "Hi" or text == "hi":
        reply = 'Hello'

    elif text == "今天課表" or text == "today":
        reply = command.today()


    elif text == "下節課" or text == "next":
        reply = command.next_lesson()

    elif "help" in text:
        decision = text[5:]
        reply = command.help(decision)

    elif "hw" in text:
        if 'rm' in text:
            HW = text[6:]
            if text == "hw rm all":
                reply = command.remove_all_homework()
            elif HW == ' ' or HW == '':
                reply = '[未輸入刪除行號]'
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

    elif 'tc' in text:

        if text == "tc rm":
            reply = command.remove_all_transClass()

        elif "add" in text:
            CL = text[10:]
            reply = command.add_transClass(CL)

        elif text == "tc" or text == "tc ":
            reply = command.print_transClass()

    elif "test" in text:
        if 'rm' in text:
            Test = text[8:]
            if text == "test rm all":
                reply = command.remove_all_test()
            elif Test == ' ' or Test == '':
                reply = '[未輸入刪除行號]'
            else:
                reply = command.remove_test(Test)

        elif "add" in text:
            Test = text[9:]
            if Test == '' or Test == ' ':
                reply = '未輸入考試\n[bot test add (日期) (考試)]'
            else:
                reply = command.add_test(Test)
        elif text == "test" or text == "test ":
            reply = command.print_test()

    else:
        reply = '未知指令\n[bot help可查詢指令]'

    return reply

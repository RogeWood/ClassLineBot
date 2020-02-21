from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
)
import command

def reply_Text_Message(text):
    homework = text[:6]

    if text == "bot Hi" or text == "bot hi":
        reply = 'Hello'

    elif text == "bot 今天課表":
        reply = command.today_lesson()

    elif text == "bot help":
        reply = command.help()

    elif text == "bot 下節課" or text == "bot next":
        reply = command.next_lesson()

    elif text == "bot time":
        time = datetime.now()
        reply = str(time.hour+8) + ':'+str(time.minute)

    elif homework == "bot hw":
        if text == "bot hw rm":
            reply = command.remove_homework()
        elif text == "bot hw rm all":
            reply = command.remove_all_homework()
        elif "add" in text:
            HW = text[11:]
            if HW == '' or HW == ' ':
                reply = '[bot hw add (作業)]'
            else:
                reply = command.add_homework(HW)
        elif text == "bot hw" or text == "bot hw ":
            reply = command.print_homework()

    else:
        reply = '未知指令\nbot help可查詢指令'

    return reply

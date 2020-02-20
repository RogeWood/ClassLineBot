from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
)
import json

app = Flask(__name__)

#Channel secret
line_bot_api = LineBotApi('YMvWMbuo2BxWlEqgda3ObZVz1l5DtTAOFGiiGFg0XCJ1pN2lGBz8koNWNaykUwYAPfHvxq46L5fGmzfqthOuv1Ix8JB6iRZj0kEynIHdTKfbyJWTnggeUBn5VUfqgF5mwWOXO3w6CZdJgv911mdmjwdB04t89/1O/w1cDnyilFU=')
#token
handler = WebhookHandler('c946fa7e673733b54133119ad667ee0a')


@app.route("/")
def home():
    return 'home OK'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    check = text[:3]

    if check == "bot":

        if text == "bot Hi" or text == "bot hi":
            message = TextSendMessage('Hello')

        if text == "bot help":
            with open("command.txt", mode='r', encoding="utf-8") as file:
                data = file.read()
            message = TextSendMessage(data)

        elif text == "bot 課表":
            message = ImageSendMessage(
                original_content_url='https://i.imgur.com/jbAn2m4.jpg',
                preview_image_url='https://i.imgur.com/jbAn2m4.jpg')

        else:
            message = TextSendMessage('未知指令\nbot help可查詢指令')


        line_bot_api.reply_message(event.reply_token, message)



if __name__ == "__main__":
    app.run()

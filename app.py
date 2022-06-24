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
import json, Reply, os
from dotenv import load_dotenv
app = Flask(__name__)

#webhook
#https://class-bot123.herokuapp.com/callback
# if use ngrok needs to add /callback

# load env
load_dotenv()
#Channel secret
line_bot_api = LineBotApi(os.getenv("LINE_BOT_API"))
#token
handler = WebhookHandler(os.getenv('WEBHOOK_TOKEN'))


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

    if check == "bot" or check == "Bot":
        handle_text = text[4:]

        if handle_text == "課表":
            message = ImageSendMessage(
                original_content_url='https://i.imgur.com/jbAn2m4.jpg',
                preview_image_url='https://i.imgur.com/jbAn2m4.jpg')

        else: #回傳文字
            reply = Reply.reply_Text_Message(handle_text)
            message = TextSendMessage(reply)


    line_bot_api.reply_message(event.reply_token, message)



if __name__ == "__main__":
    app.run()

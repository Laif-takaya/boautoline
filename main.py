from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import sousa

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = "KMVTxjxp7pxbUHk9Xb4uL0v8/1rDvOJUOfAR5tp18ImgWBJn349FApfcqyR2xmStAYoabAyfTpcAv5AyJAF0Fq+sFJKddUVgPo+cSbXk3YucNLlYHXEt+wd+0BngdGyWcKUXMXkDcjYFDWYS9J1zfAdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "51eaf0af063d62d67140f01297f1b310"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    date = event.message.text

    # アイテム取得関数を呼び出し
    result = sousa.highLow(date)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

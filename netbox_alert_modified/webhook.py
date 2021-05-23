from flask import Flask, request, abort
import telebot
import requests
import config
app = Flask(__name__)

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

@app.route('/webhook/<path>', methods=['POST'])
def webhook(path):
    try:
        if request.method == 'POST':
            procees = request.json.get('event')
            model = request.json.get('model')
            data = request.json.get('data')
            username = request.json.get('username')
            message = "Event: " + str(procees) + "\n" + "Object: " + str(model) + "\n" + "User: " +str(username) + "\n\n\n" + "Data: " + "\n" +str(data)
            if config.TELEGRAM_TOKEN != "" and config.TELEGRAM_CHAT_ID != "":
                telegram_bot_sendtext(message)
            if config.SLACK_TOKEN != "" and config.SLACK_CHANNEL != "":
                slack_bot_sendtext(message)
            return path, 200
        else:
            abort(400)
    except Exception as ex:
        abort(400)

def telegram_bot_sendtext(message):
    print(message)
    send_text = bot.send_message(config.TELEGRAM_CHAT_ID, message)
    response = requests.get(send_text)
    return response.json()

def slack_bot_sendtext(message):
    slack_token = config.SLACK_TOKEN
    slack_channel = config.SLACK_CHANNEL
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': message,
    }).json()

if __name__ == '__main__':
    app.run(host= '0.0.0.0')

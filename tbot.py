import requests
import datetime
from time import sleep

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates_json(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.api_url + method, data=params)
        result_resp = response.json()["result"]
        return result_resp

    def get_last_update(self):
        result = self.get_updates_json()
        length_res = len(result)

        if length_res>0:
            last_update = result[-1]
        else:
            last_update = result[length_res]
        return  last_update

    def get_chat_id(update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_mess(self, chat, text):
        params = {'chat_id': chat, 'text':text}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, data=params)
        return  response

token = "712151390:AAFM2bGZICQhLFtn0P75WTqlO4WXZk5PCTw"
greet_bot = BotHandler(token)
hi_text = ("привет", "здравствуй", "ку", "hello", "hi", "q")
time_text = ("сколько время", "время", "дата", "date", "time")
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates_json(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        if last_chat_text.lower() in hi_text:
            greet_bot.send_mess(last_chat_id, "Привет, друг {}".format(last_chat_name))
        if last_chat_text.lower() in time_text:
            greet_bot.send_mess(last_chat_id, "Сегодня {today}, время {hour}".format(today=today, hour=hour))
        new_offset = last_update_id+1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
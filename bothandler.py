import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates_json(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.api_url + method, data=params)
        print(response.json())
        result_resp = response.json()["result"]
        return result_resp

    def get_last_update(self):
        result = self.get_updates_json()

        if len(result)>0:
            last_update = result[-1]
        else:
            last_update = None
        return last_update

    def get_chat_id(update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_message(self, chat, text):
        params = {'chat_id': chat, 'text':text}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, data=params)
        return response

    def send_photo(self, chat, photo):
        params = {'chat_id': chat, 'photo': photo}
        method = 'sendPhoto'
        response = requests.post(self.api_url + method, data=params)
        return response

    def send_message_with_buttons(self, chat):
        keyboard = InlineKeyboardMarkup()
        hi_button = InlineKeyboardButton(text="Hello")
        reg_button = InlineKeyboardButton(text="Registration")
        keyboard.add(hi_button)
        keyboard.add(reg_button)
        params = {'chat_id':chat, 'text':'OK', 'reply_markup':hi_button}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, data=params)
        return response

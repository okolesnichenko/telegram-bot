import requests
import json

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

    def send_photo_with_caption(self, chat, photo, caption):
        params = {'chat_id':chat, 'photo':photo, 'caption':caption}
        method = 'sendPhoto'
        response = requests.post(self.api_url + method, data=params)
        return response

    def send_user_photo(self, chat, photo, caption, name):
        buttons = json.dumps({'inline_keyboard': [[{'text': 'Like', 'callback_data': 'like'},
                                                   {'text': 'Next', 'callback_data': 'next'}]]})
        text = name + '\n' + caption
        params = {'chat_id': chat, 'photo': photo, 'caption': text, 'reply_markup':buttons}
        method = 'sendPhoto'
        response = requests.post(self.api_url + method, data=params)
        return response

    def send_message_with_menu_buttons(self, chat, text):
        # Old method, later i will change it TO DO (4)
        buttons = json.dumps({'inline_keyboard': [[{'text': 'Game', 'callback_data': 'game'},
                                                   {'text':'Registration', 'callback_data': 'registration'},
                                                   {'text': 'Rules', 'callback_data': 'rules'},
                                                   {'text':'About us', 'callback_data': 'about'}]]})
        params = {'chat_id':chat, 'text':text, 'reply_markup':buttons}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, data=params)
        return response

    def send_message_with_sex_buttons(self, chat, text):
        # Old method, later i will change it TO DO (4)
        buttons = json.dumps({'inline_keyboard': [[{'text': 'Male', 'callback_data': 'male'},
                                                   {'text':'Female', 'callback_data': 'female'}]]})
        params = {'chat_id':chat, 'text':text, 'reply_markup':buttons}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, data=params)
        return response

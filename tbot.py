import requests
import datetime
import random
import os
import sqlite3
from time import sleep

conn = sqlite3.connect('model.db')
c = conn.cursor()

hi_text = ("привет", "здравствуй", "ку", "hello", "hi", "q")
time_text = ("сколько время", "время", "дата", "date", "time")
photo_text = ("фото", "фотография", "photo", "next")
photoIdList = []

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

class BotOptions:
    def __init__(self, greet_bot):
        self.greet_bot = greet_bot

    def say_something(self, last_update, photoIdList, time):
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        if last_chat_text.lower() in time_text:
                self.greet_bot.send_message(last_chat_id, "Сегодня {today}, время {hour}:{minute}"
                                       .format(today=time['today'], hour=time['hour'], minute=time['minute']))
        if last_chat_text.lower() in hi_text:
            self.greet_bot.send_message(last_chat_id, "Привет, друг {}".format(last_chat_name))
        if last_chat_text.lower() in photo_text:
            print(photoIdList)
            if (photoIdList):
                self.greet_bot.send_photo(last_chat_id, random.choice(photoIdList))
        return last_update_id

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS model(name TEXT, sex TEXT, age INTEGER, photo TEXT)")

def get_time():
    now = datetime.datetime.now()
    today = now.day
    hour = now.hour + 3
    minute = now.minute
    data = {"today": today, "hour": hour, "minute": minute}
    return data

def main():
    greet_bot = BotHandler(os.getenv("TOKEN"))
    bot = BotOptions(greet_bot)
    new_offset = None
    arr = []
    create_table()
    while True:
        greet_bot.get_updates_json(new_offset)
        last_update = greet_bot.get_last_update()
        time = get_time()
        if(last_update):
            last_update_id = last_update['update_id']
            if (last_update['message'].get('text')):
                bot.say_something(last_update, photoIdList, time)
                arr.append("Oleg")
                arr.append("man")
                arr.append(13)
                arr.append("asasas")
                c.execute("INSERT INTO model VALUES(?,?,?,?)", arr)
                arr.clear()
                conn.commit()
            if (last_update['message'].get('photo')):
                last_photo_id = last_update['message']['photo'][0]['file_id']
                photoIdList.append(last_photo_id)
                print(photoIdList)
            new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
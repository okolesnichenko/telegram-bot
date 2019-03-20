import random

hi_text = ("привет", "здравствуй", "ку", "hello", "hi", "q")
time_text = ("сколько время", "время", "дата", "date", "time")
photo_text = ("фото", "фотография", "photo", "next")
reg_text = ("регистрация", "зарегестрироваться", "рег")


class BotOptions:
    def __init__(self, greet_bot, db):
        self.greet_bot = greet_bot
        self.database = db

    def registration(self, last_update):
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_username = last_update['message']['chat']['username']
        photo = 'somephoto'
        data = {'username':last_chat_username, 'name':last_chat_name, 'photo':photo}
        self.database.add_user(data)

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
        if last_chat_text.lower() in reg_text:
            self.registration(last_update)
        return last_update_id
import random

hi_text = ("привет", "здравствуй", "ку", "hello", "hi", "q")
time_text = ("сколько время", "время", "дата", "date", "time")
reg_text = ("регистрация", "зарегестрироваться", "рег", "registration")


class BotOptions:
    def __init__(self, greet_bot, db):
        self.greet_bot = greet_bot
        self.database = db

    def get_user_data(self, last_update):
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_username = last_update['message']['chat']['username']
        # Необходимо поулчить file_id от отправленной фото
        # и передать его для добавления в бд
        photo = ''
        data = {'username':last_chat_username, 'name':last_chat_name, 'photo':photo}
        return data

    def say_something(self, last_update, photoIdList, time):
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        # Type "time"
        if last_chat_text.lower() in time_text:
                self.greet_bot.send_message(last_chat_id, "Сегодня {today}, время {hour}:{minute}"
                                       .format(today=time['today'], hour=time['hour'], minute=time['minute']))
        # Type "hi"
        if last_chat_text.lower() in hi_text:
            self.greet_bot.send_message(last_chat_id, "Привет, друг {}".format(last_chat_name))
        # Type "registration"
        if last_chat_text.lower() in reg_text:
            self.greet_bot.send_message(last_chat_id, "Send photo")
            # Get username and name
            data = self.get_user_data(last_update)
            print(data)
            # Wait photo!
            # TO DO
        return last_update_id

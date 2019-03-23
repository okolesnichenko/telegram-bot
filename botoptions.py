import random

hi_text = ("привет", "здравствуй", "ку", "hello", "hi", "q")
time_text = ("сколько время", "время", "дата", "date", "time")
reg_text = ("регистрация", "зарегестрироваться", "рег", "registration")


class BotOptions:
    def __init__(self, greet_bot, db):
        self.greet_bot = greet_bot
        self.database = db

    # Delete after reg realisation TO DO
    def get_user_data(self, last_update):
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_username = last_update['message']['chat']['username']
        # Необходимо поулчить file_id от отправленной фото
        # и передать его для добавления в бд
        data = {'username':last_chat_username, 'name':last_chat_name, 'photo':''}
        return data

    def get_photo_and_data(self, last_update):
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_username = last_update['message']['chat']['username']
        last_photo_id = last_update['message']['photo'][0]['file_id']
        data = {'username': last_chat_username, 'name': last_chat_name, 'photo': last_photo_id}
        return data

    def menu_switcher(self, last_update):
        # Here is switch callback (1: hello, 2: registratiom, 3:rules, 4:about us)
        keys = ('hello', 'registration', 'rules', 'about')
        data = last_update['callback_query']['data']
        # This is bad TO DO
        if (data == keys[0]):
            pass
        elif (data == keys[1]):
            pass
        elif (data == keys[2]):
            pass
        elif (data == keys[3]):
            pass
        print(data)

    def say_something(self, last_update, time):
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        # Type "time"
        if last_chat_text.lower() in time_text:
                self.greet_bot.send_message(last_chat_id, "Today {today}, time {hour}:{minute}"
                                       .format(today=time['today'], hour=time['hour'], minute=time['minute']))
        # Type "hi"
        if last_chat_text.lower() in hi_text:
            # Send buttons
            self.greet_bot.send_message_with_buttons(last_chat_id, "Hello {}, make a choice:".format(last_chat_name))
        # Type "registration"
        if last_chat_text.lower() in reg_text:
            self.greet_bot.send_message(last_chat_id, "Send photo")
            # Wait photo!
            # TO DO
        return last_update_id

import random

hi_text = ("привет", "здравствуй", "ку", "hello", "hi", "q")
time_text = ("сколько время", "время", "дата", "date", "time")
reg_text = ("регистрация", "зарегестрироваться", "рег", "registration")
userdata = {'username': '', 'name': '', 'sex': '', 'photo': '', 'description':''}
users_list = [{}]

''' 
1) i can create list of userdata
add userdata with username and after it add next info about this user

or
2) i need asynk io 


now i will do first
'''

class BotOptions:
    def __init__(self, greet_bot, db):
        self.greet_bot = greet_bot
        self.database = db

    # And add try exept everywhere TO DO (2)
    def game(self, last_update):
        last_chat_id = last_update['message']['chat']['id']
        data = self.database.get_users()
        for user in data:
            self.greet_bot.send_photo_with_caption(last_chat_id, user.get('photo'), user.get('description'))
        print(data)

    def get_photo_and_data(self, last_update):
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_username = last_update['message']['chat']['username']
        last_photo_id = last_update['message']['photo'][0]['file_id']
        last_photo_caption = last_update['message'].get('caption')
        for user in users_list:
            if (user.get('username')==last_chat_username):
                user['username'] = last_chat_username
                user['name'] = last_chat_name
                #user['sex'] -> in menu switcher
                user['photo'] = last_photo_id
                user['description'] = last_photo_caption
                return user
        return None

    def menu_switcher(self, last_update):
        # Here is switch callback (1: hello, 2: registratiom, 3:rules, 4:about us)
        userdata = {'username': '', 'name': '', 'sex': '', 'photo': '', 'description':''}
        keys = ('hello', 'registration', 'rules', 'about', 'male', 'female')
        data = last_update['callback_query']['data']
        last_chat_id = last_update['callback_query']['message']['chat']['id']
        last_chat_name = last_update['callback_query']['message']['chat']['first_name']
        last_chat_username = last_update['callback_query']['message']['chat']['username']
        # This is bad TO DO (3)
        if (data == keys[0]):
            self.greet_bot.send_message(last_chat_id, "Hello {}, my friend. Let's play!".format(last_chat_name))
            self.game(last_update)
        elif (data == keys[1]):
            userdata['username'] = last_chat_username
            users_list.append(userdata)
            self.greet_bot.send_message_with_sex_buttons(last_chat_id, "Choose sex:")
        elif (data == keys[2]):
            self.greet_bot.send_message(last_chat_id, "Please don't spam to this bot. Thank you.".format(last_chat_name))
        elif (data == keys[3]):
            self.greet_bot.send_message(last_chat_id, "I am junior python developer. "
                                                      "Here is my application. You are welcome {}.".format(last_chat_name))
        elif (data == keys[4]):
            for user in users_list:
                if (user.get('username')==last_chat_username):
                    user['sex'] = keys[4]
            self.greet_bot.send_message(last_chat_id, "Send photo for profile in game "
                                                      "and add the caption(your description - briefly about yourself):")
        elif (data == keys[5]):
            for user in users_list:
                if (user.get('username')==last_chat_username):
                    user['sex'] = keys[5]
            self.greet_bot.send_message(last_chat_id, "Send photo for profile in game "
                                                      "and add the caption(your description - briefly about yourself):")
        print(data)

    def say_something(self, last_update, time):
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        # Type "hi"
        if last_chat_text.lower() in hi_text:
            # Send buttons
            self.greet_bot.send_message_with_menu_buttons(last_chat_id, "Hello {}, make a choice:".format(last_chat_name))
        # Type "registration"
        if last_chat_text.lower() in reg_text:
            self.greet_bot.send_message_with_sex_butons(last_chat_id, "Choose sex:")
            self.greet_bot.send_message(last_chat_id, "And after it send photo")
            # Wait photo!
            # TO DO
        return last_update_id

import datetime
import os
from botoptions import BotOptions
from dboperations import DataBaseOperations
from bothandler import BotHandler

photoIdList = []

def get_time():
    now = datetime.datetime.now()
    today = now.day
    hour = now.hour + 3
    minute = now.minute
    data = {"today": today, "hour": hour, "minute": minute}
    return data

def main():
    db = DataBaseOperations(os.environ['DATABASE_URL'])
    greet_bot = BotHandler(os.getenv("TOKEN"))
    bot = BotOptions(greet_bot, db)
    new_offset = None
    while True:
        greet_bot.get_updates_json(new_offset)
        last_update = greet_bot.get_last_update()
        time = get_time()
        if(last_update):
            last_update_id = last_update['update_id']
            # If message type is text ->
            if (last_update['message'].get('text')):
                data = bot.say_something(last_update, photoIdList, time)
            # If message type is photo (file) ->
            if (last_update['message'].get('photo')):
                if(data.get('username')):
                    bot.get_photo_and_data(last_update)
                    db.add_user(data)
                    data = {}

            new_offset = last_update_id + 1
    cur.close()
    conn.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

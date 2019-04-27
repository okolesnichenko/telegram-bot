import speech_recognition as sr

def recognize(file):

    try:
        usertext = r.recognize_google(file, language="ru_RU").lower()
        print(format(usertext))
    except sr.UnknownValueError:
        print("Скаже еще")
        usertext = "Аудио не распознано"
    return usertext

import speech_recognition as sr

def recognize(file):
    r = sr.Recognizer()
    #with sr.AudioFile(file) as source:
    #    audio = r.record(source)
    try:
        usertext = r.recognize_google(file, language="ru_RU").lower()
        print(format(usertext))
    except sr.UnknownValueError:
        print("Скаже еще")
        usertext = "Аудио не распознано"
    return usertext

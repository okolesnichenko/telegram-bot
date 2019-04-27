import speech_recognition as sr

def recognize(file):
    with sr.AudioFile(file) as source:
        r = sr.Recognizer()
        audio = r.record(source)
    try:
        usertext = r.recognize_google(audio, language="ru_RU").lower()
        print(format(usertext))
    except sr.UnknownValueError:
        print("Скаже еще")
        usertext = "Аудио не распознано"
    return usertext

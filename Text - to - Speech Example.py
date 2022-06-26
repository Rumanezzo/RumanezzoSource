import pyttsx3
import speech_recognition as sr
from random import choice


engine = pyttsx3.init()
r = sr.Recognizer()


def talk(text):
    print(text)

    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print('Говорите...')

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='ru-Ru')
        except sr.UnknownValueError:
            text = 'Не расслышала...'

        print(text)
        return text


user_name = ''

while True:
    st = listen()
    st = st.lower()

    if st in ('привет', 'здравствуй', 'приветик', 'hello', 'хай'):
        talk(choice(('И тебе не хворать!', 'Привет, привет...!', 'День добрый!')))

    if st in ('как тебя зовут', 'как твоё имя', 'кто ты'):
        talk('Меня зовут Марина-киборг, а как Ваше имя?')
        user_name = listen()
        talk('Очень приятно!')

    if st in ('пока-пока', 'пока', 'до свидания'):
        break

talk(f'До скорого свидания!...{user_name}')

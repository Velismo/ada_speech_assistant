import speech_recognition as sr
from time import ctime

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Lo siento, no te he entendido')
        except sr.RequestError:
            print('Lo siento, el sistema no funciona correctamente')
        return voice_data

def respond(voice_data):
    if '¿Cómo te llamas?' in voice_data:
        print('Me llamo Ada')
    if '¿Qué hora es?' in voice_data:
        print(ctime())

print('¿Cómo puedo ayudarte?')
voice_data = record_audio()
respond(voice_data)
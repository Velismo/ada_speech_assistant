import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
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
    if 'buscar' in voice_data:
        search = record_audio('¿Qué quieres buscar?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Esto es lo que he encontrado por ' + search)
    if 'encontrar' in voice_data:
        location = record_audio('¿Qué quieres localizar?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Esto es lo que he encontrado por ' + location)
    if 'salir' in voice_data:
        exit()

time.sleep(1)
print('¿Cómo puedo ayudarte?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
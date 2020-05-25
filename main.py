import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Di algo')
    audio = r.listen(source)
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        print('Lo siento, no te he entendido')

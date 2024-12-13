import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "audio.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)
        said = ""

        try:
            said = recog.recognize_google(audio)
            print("Said: " + said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

online = True
while online:
    text = get_audio()
    if "Jarvis clip that" in text:
        speak("Received")
        #print("Received")
    elif "Jarvis shutdown" in text or "Jarvis shut down" in text:
        speak("Offline")
        #print("Offline")
        online = False

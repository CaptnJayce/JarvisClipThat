import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


# call speak and input what the TTS should say
# save output as "test.mp3"
def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "test.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
speak("Test")
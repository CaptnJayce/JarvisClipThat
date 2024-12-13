import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# call speak and input what the TTS should say
# save output as "test.mp3"
def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "audio.mp3"
    tts.save(filename)
    playsound.playsound(filename)    

def get_audio():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recog.listen(source)
        said = ""
        
        try:
            said = recog.recognize_google(audio)
            print(said)
        except Exception as e:
            print("exception: " + str(e))

    return said

text = get_audio()
if "Jarvis clip that" in text:
    speak("Recieved")

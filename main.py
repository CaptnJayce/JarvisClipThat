import os
import time
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from pynput.keyboard import Key, Controller

keyboard = Controller()

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

while True:
    text = get_audio()
    if "Jarvis" in text and "clip" in text:
        sound = AudioSegment.from_file("audio/done.mp3")
        play(sound)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.press('S')
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release('S')

    elif "Jarvis" in text and "shut down" or "Jarvis" in text and "shutdown" in text:
        sound = AudioSegment.from_file("audio/shutdown.mp3")
        play(sound)
        break
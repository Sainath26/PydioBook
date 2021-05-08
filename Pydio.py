import pyttsx3
import pyperclip

audio = pyttsx3.init()
audio.setProperty('rate',125)
audio.say(pyperclip.paste())
audio.runAndWait()

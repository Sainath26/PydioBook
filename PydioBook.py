import pyttsx3
import pyperclip



audio = pyttsx3.init()
audio.setProperty('rate',170)

audio.save_to_file(pyperclip.paste(),'txct.mp3')
audio.runAndWait()

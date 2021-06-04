from flask import Blueprint, render_template
import pyttsx3


audio = pyttsx3.init()
a = ''
audio.setProperty('rate',125)
audio.say(a)
audio.runAndWait()

views = Blueprint('views',__name__)


@views.route('/')
def home():
    return render_template("home.html")









    views = Blueprint('views',__name__)

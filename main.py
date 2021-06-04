#This is the main file. This file is used to run the server
from flask import Blueprint, render_template
from pydio import create_app 
import pyttsx3
from flask import request

app = create_app()
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")




@app.route('/conv',methods=['POST'])
def conv():
    while True:
        if request.method == 'POST':
            text = request.form.get("t")
        
            audio = pyttsx3.init()
    
            audio.setProperty('rate',150)
            audio.say(text)
            audio.runAndWait()
        



if __name__ == '__main__':
    app.run(debug=True)
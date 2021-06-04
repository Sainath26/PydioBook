#This is the main file. This file is used to run the server
from pydio import create_app 
import pyttsx3
from flask import request

app = create_app()




@app.route('/conv',methods=['POST'])
def conv():
    if request.method == 'POST':
        text = request.form.get("t")
        audio = pyttsx3.init()
        audio.setProperty('rate',125)
        audio.say(text)
        audio.runAndWait()



if __name__ == '__main__':
    app.run(debug=True)
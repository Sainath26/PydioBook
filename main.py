from flask import Blueprint, render_template

import pyttsx3


from flask import Flask,request,render_template
app =Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')




@app.route('/conv',methods=['POST'])
def conv():
    bool = True
    while bool==True:    
        text = request.form.get("t")
            
        audio = pyttsx3.init()
        
        audio.setProperty('rate',150)
        audio.say(text)
        audio.runAndWait()
        break

    return render_template('index.html')
        



if __name__ == '__main__':
    app.run(debug=True)
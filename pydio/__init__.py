#This file makes the whole pydio folder a package
from flask import Flask
from.views import views
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chummaorukey'

    

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix = '/')



    return app
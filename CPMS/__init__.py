# from CPMS.models import Author
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = 'iTried'
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  
    db.init_app(myapp)

    from .app import app

    myapp.register_blueprint(app, url_prefix='/')

    from .models import Author, Reviewer

    # create DB
    create_database(myapp)

    login_manager = LoginManager()
    login_manager.login_view = 'app.LoginForm'
    login_manager.init_app(myapp)

    @login_manager.user_loader
    def load_user(id):

        if Reviewer.query.get(int(id)):
            print("reviewer found")
            return Reviewer.query.get(int(id))

        elif Author.query.get(int(id)):
            print("author found")
            return Author.query.get(int(id))

        else:
            print('ERROR')
        # login reviewer

    return myapp


# database setup
def create_database(app):
    # if no db found in directory, create a new one
    # might not work on different os
    if not path.exists('CPSM/' + DB_NAME): 
        db.create_all(app=app)
        # print('DB Created')


# from CPMS.models import Author
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = 'iTried'
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:MICHAELTAVERASD/LendApp' #add correct database
    db.init_app(myapp)

    from .app import app

    myapp.register_blueprint(app, url_prefix='/')

    from .models import Author

    # create DB

    login_manager = LoginManager()
    login_manager.login_view = 'app.LoginForm'
    login_manager.init_app(myapp)

    @login_manager.user_loader
    def load_user(id):
        return Author.query.get(int(id))

    return myapp




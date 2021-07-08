from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = 'iTried'
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:MICHAELTAVERASD/LendApp' #add correct database
    

    db.init_app(myapp)

    from .app import app

    myapp.register_blueprint(app, url_prefix='/')

    return myapp




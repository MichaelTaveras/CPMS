from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:MICHAELTAVERASD/LendApp'
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False
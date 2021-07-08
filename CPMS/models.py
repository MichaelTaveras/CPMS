from . import db
from flask_login import UserMixin

class Author(db.Model, UserMixin):
    AuthorID = db.Column(db.integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    MiddleInitial = db.Column(db.String(1))
    LastName = db.Column(db.String(50))
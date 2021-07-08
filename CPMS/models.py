from . import db
from flask_login import UserMixin

# model for author
class Author(db.Model, UserMixin):
    AuthorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    MiddleInitial = db.Column(db.String(1))
    LastName = db.Column(db.String(50))
    Affiliation = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    Address = db.Column(db.String(50))
    City = db.Column(db.String(50))
    State = db.Column(db.String(2))
    ZipCode = db.Column(db.String(10))
    PhoneNumber = db.Column(db.String(50))
    EmailAddress = db.Column(db.String(100))
    Password = db.Column(db.String(5))
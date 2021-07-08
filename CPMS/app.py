from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash, session
import sqlalchemy
from .models import Author
from werkzeug.security import generate_password_hash, check_password_hash # hides password
from . import db


app = Flask(__name__ )
app.config['SECRET_KEY'] = 'iTried'

@app.route('/')
def index():
    return render_template('PaperPage.html')

@app.route('/AccountSettings')
def AccountSettings():
    return render_template('AccountSettings.html')

@app.route('/authorViewForm')
def authorViewForm():
    return render_template('authorViewForm.html')

@app.route('/Forgot')
def Forgot():
    return render_template('Forgot.html')

@app.route('/LoginForm', methods=['GET','POST'])
def LoginForm():
    if request.method == 'POST':
        email = request.form.get('EmailAddress')
        password = request.form.get('Password')

        author = Author.query.filter_by(EmailAddress='email').first()

        if author:
            if check_password_hash(author.Password, password):
                 flash('You have been successfully logged in.', category='succes')
                 return redirect(url_for('index'))
            else:
                 flash('Wrong password. Please try again.', category='error')
        else:
            flash('Email does not exist.  Please try again.', category='error')

    return render_template('LoginForm.html')
        

@app.route('/Management')
def Management():
    return render_template('Management.html')

@app.route('/PaperPage')
def PaperPage():
    return render_template('PaperPage.html')

@app.route('/PaperReview')
def PaperReview():
    return render_template('PaperReview.html')

@app.route('/paperSubmitForm')
def paperSubmitForm():
    return render_template('paperSubmitForm.html')

@app.route('/RegistrationForm',methods=['GET','POST'])
def RegistrationForm():
    if request.method == 'POST':
        fname = request.form.get('FirstName')
        midIn = request.form.get('MiddleInitial')
        lname = request.form.get('LastName')

        affil = request.form.get('Affiliation')
        dep = request.form.get('Department')
        
        address = request.form.get('Address')
        city = request.form.get('City')
        state = request.form.get('State')
        zip = request.form.get('Zip')

        email = request.form.get('EmailAddress')
        phone = request.form.get('PhoneNumber')
        password = request.form.get('Password')

        author = Author.query.filter_by(EmailAddress='email').first()

        if author:
            flash("Email already exits. Try again.", category='error')
        if len(email) < 5:
            flash('Email must be greater than 5 characters.', category='error')
           
        elif len(password) != 5:
           flash('Password must be 5 characters.', category='error')
        else:
            newAuthor = Author(
                FirstName = fname,
                MiddleInitial = midIn,
                LastName = lname,
                Affiliation = affil,
                Department = dep,
                Address = address,
                City = city,
                State = state,
                ZipCode = zip,
                EmailAddress = email,
                PhoneNumber = phone,
                Password = generate_password_hash(password, method='sha256'))

            # to database
            # db.session.add(newAuthor)
            # db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('index'))
            



    return render_template('RegistrationForm.html')

@app.route('/reviewerViewForm')
def reviewerViewForm():
    return render_template('reviewerViewForm.html')

@app.route('/reviewSubmitForm')
def reviewSubmitForm():
    return render_template('reviewSubmitForm.html')

@app.route('/viewForm')
def viewForm():
    return render_template('viewForm.html')

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="localhost", port=8010, debug=True)

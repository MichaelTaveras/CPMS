from os import remove
from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash, session, Blueprint
import sqlalchemy
from sqlalchemy.sql.functions import user
from .models import Author, Reviewer
from werkzeug.security import generate_password_hash, check_password_hash # hides password
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# user=current_user  -> links current user to each template


app = Blueprint('app', __name__)

@app.route('/LoginForm', methods=['GET','POST'])
def LoginForm():
    if request.method == 'POST':
        email = request.form.get('EmailAddress')
        password = request.form.get('Password')
        remember  = request.form.get('remember')

        # looks for user in DB
        author = Author.query.filter_by(EmailAddress=email).first()
        reviewer = Reviewer.query.filter_by(EmailAddress=email).first()

        # if user found checks password
        # if wrong password throw error
        # if user not found throw error
        print(email)
        print(author)
        if author:
            if check_password_hash(author.Password, password):
                 flash('You have been successfully logged in.', category='succes')
                 login_user(author, remember=remember)
                 return redirect(url_for('app.index', user=current_user))
            else:
                 flash('Wrong password. Please try again.', category='error')
        elif reviewer:
            if check_password_hash(reviewer.Password, password):
                 flash('You have been successfully logged in.', category='succes')
                 login_user(reviewer, remember=remember)
                 return redirect(url_for('app.index'))
            else:
                 flash('Wrong password. Please try again.', category='error')
        else:
            flash('Email does not exist.  Please try again.', category='error')

    return render_template('LoginForm.html', user=current_user)


@app.route('/Forgot')
def Forgot():
    return render_template('Forgot.html')


@app.route('/RegistrationForm',methods=['GET','POST'])
def RegistrationForm():
    if request.method == 'POST':
        userType = request.form.get('type')
        
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

        

        author = Author.query.filter_by(EmailAddress=email).first()
        reviewer = Reviewer.query.filter_by(EmailAddress=email).first()

        if author or reviewer:
            flash("Email already exits. Try again.", category='error')
        if len(email) < 5:
            flash('Email must be greater than 5 characters.', category='error')
           
        elif len(password) != 5:
           flash('Password must be 5 characters.', category='error')
        else:
            if userType == 'author':
                newUser = Author(
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
            elif userType == 'reviewer':
                newUser = Reviewer(
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
            else:
                print("Error on user type")
            # to database
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('app.index'))
            

    return render_template('RegistrationForm.html', user=current_user)


# //////////////////////////////////////////////////////////////////////


# TODO: THESE TEMPLATES NEED TO BE IMPLEMENTED WHICH USER INFO


@app.route('/')
@login_required #cant access page unless user logged in
def index():
    # have correct things chow depending on user
    return render_template('PaperPage.html', user=current_user)


@app.route('/AccountSettings',methods=['GET','POST'])
@login_required
def AccountSettings():



    return render_template('AccountSettings.html', user=current_user)


@app.route('/authorViewForm')
@login_required
def authorViewForm():
    return render_template('authorViewForm.html',user=current_user)


@app.route('/logout')
@login_required #cant access page unless user logged in
def LogOut():
    logout_user()
    return redirect(url_for('app.LoginForm'))

@app.route('/Management')
@login_required
def Management():
    return render_template('Management.html',user=current_user)

@app.route('/PaperPage')
@login_required
def PaperPage():
    return render_template('PaperPage.html',user=current_user)

@app.route('/PaperReview')
@login_required
def PaperReview():
    return render_template('PaperReview.html',user=current_user)

@app.route('/paperSubmitForm')
@login_required
def paperSubmitForm():
    return render_template('paperSubmitForm.html',user=current_user)


@app.route('/reviewerViewForm')
@login_required
def reviewerViewForm():
    return render_template('reviewerViewForm.html',user=current_user)


@app.route('/reviewSubmitForm')
@login_required
def reviewSubmitForm():
    return render_template('reviewSubmitForm.html',user=current_user)


@app.route('/viewForm')
@login_required
def viewForm():
    return render_template('viewForm.html',user=current_user)




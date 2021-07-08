from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash, session
import sqlalchemy
import re

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
    # data = request.form
    # print(data)

    # msg = ''
    # if request.method == 'POST':
    #     results = log_in(db, dict(request.form))
    #     if not results:
    #         flash('Wrong login information. Please try again.')
    #         return render_template('LoginForm.html')
    #     flash('You have been successfully logged in.')
    #     return redirect(url_for('PaperPage'), msg = msg)

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

        if len(email) < 5:
            flash('Email must be greater than 5 characters.', category='error')
           
        elif len(password) != 5:
           flash('Password must be 5 characters.', category='error')
        else:
            pass
            # to database



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

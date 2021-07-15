from os import remove
from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash, session, Blueprint
import sqlalchemy
from sqlalchemy.sql.functions import user
from sqlalchemy.inspection import inspect
from .models import Author, Review, Reviewer, Paper
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
        
        if author:
            if check_password_hash(author.Password, password):
                 flash('You have been successfully logged in.', category='succes')
                 login_user(author, remember=remember)
                 return redirect(url_for('app.index'))
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

    return render_template('LoginForm.html')


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
        elif len(email) < 5:
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
                    # other topics need to be added
            else:
                print("Error on user type")

            # to database
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('app.index'))
            

    return render_template('RegistrationForm.html', user=current_user)


@app.route('/paperSubmitForm', methods=['GET', 'POST'])
@login_required
def paperSubmitForm():
    if request.method == 'POST':
        title = request.form.get('Title')
        file = request.files['File']
        fileName = file.filename

        topics = request.form.getlist('topics')
        print(topics)

    
        # file.save(file.filename)
        if len(title) > 500:
            flash('Title is too long.', category='error')
        elif False == True:
            pass
        else:
            print('paper added')
            new_paper = Paper(
                Title=title, 
                AuthorID=current_user.AuthorID, 
                FileName=fileName, 
                # FileData= file
                )

            
            db.session.add(new_paper)
            db.session.commit()
            flash('Paper Submitted!', category='success')
            return redirect(url_for('app.index'))





    return render_template('paperSubmitForm.html',user=current_user)


# //////////////////////////////////////////////////////////////////////


# TODO: THESE TEMPLATES NEED TO BE IMPLEMENTED WHICH USER INFO


@app.route('/', methods=['GET', 'POST'])
@login_required #cant access page unless user logged in
def index():
    # have correct things show depending on user
   
    author = Author.query.filter_by(EmailAddress=current_user.EmailAddress).first()
    reviewer = Reviewer.query.filter_by(EmailAddress=current_user.EmailAddress).first()
  
    if author:
        userType = 'author'
    elif reviewer:
        userType = 'reviewer'

    return render_template('PaperPage.html', user=current_user, userType=userType)


@app.route('/AccountSettings',methods=['GET','POST'])
@login_required
def AccountSettings():
    # allows user to change user info

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

def get_authors():
    return Author.query.all()
    
def get_reviewers():
    return Reviewer.query.all()

def get_reviews():
    return Review.query.all()

def get_papers():
    return Paper.query.all()

@app.route('/Management', methods=['GET'])
@login_required
def Management():
    print("all authors")
    authors = get_authors()
    reviewers = get_reviewers()
    reviews = get_reviews()
    papers = get_papers()
    
    return render_template('Management.html',user=current_user, authors=authors, reviewers=reviewers, reviews=reviews, papers=papers)

@app.route('/PaperPage', methods=['GET', 'POST'])
@login_required
def PaperPage():
    return render_template('PaperPage.html',user=current_user)

@app.route('/manage_author', methods=['GET', 'POST','DELETE'])
def manage_author(x=None, y=None):
    # do something to send email
    print(request.values)
    if "delete" in request.form:
        print("delete got called")
        # author = Author(authorID)
        # db.session.delete(author)
        # db.session.commit()
    elif "edit" in request.form:
        print("edit got called")
    authors = get_authors()
    
    return render_template('Management.html',user=current_user, authors=authors)

@app.route('/PaperReview')
@login_required
def PaperReview():
    reviews = get_reviews()
    reviewers = get_reviewers()
    
    paper_ids = {}
    reviewer_ids = {}
    #fake_upload()
    #print(reviews[0].__mapper__.attrs.keys())
    for review in reviews:
        if review.PaperID not in paper_ids:
            paper_ids[review.PaperID] = [review.ReviewerID]
        else:
            paper_ids[review.PaperID].append(review.ReviewerID)
    
    output = {}
    for key, value in paper_ids.items():
        paper = Paper.query.filter_by(PaperID=key).first()
        paper_display_key = paper.Title + " " + str(paper.PaperID)
        
        for reviewer_id in value:
            reviewer = Reviewer.query.filter_by(ReviewerID=reviewer_id).first()
            if paper_display_key not in output:
                output[paper_display_key] = reviewer.FirstName + " " + reviewer.LastName
            else:
                output[paper_display_key] += ", " + reviewer.FirstName + " " + reviewer.LastName


    return render_template('PaperReview.html',user=current_user, reviews=output, reviewers=reviewers)


@app.route('/reviewerViewForm')
@login_required
def reviewerViewForm():
    return render_template('reviewerViewForm.html',user=current_user)


@app.route('/reviewSubmitForm')
@login_required
def reviewSubmitForm():
    author = Author.query.filter_by(EmailAddress=current_user.EmailAddress).first()
    reviewer = Reviewer.query.filter_by(EmailAddress=current_user.EmailAddress).first()
  
    if author:
        userType = 'author'
    elif reviewer:
        userType = 'reviewer'


    return render_template('reviewSubmitForm.html',user=current_user)


@app.route('/viewForm')
@login_required
def viewForm():
    return render_template('viewForm.html',user=current_user)


def fake_upload():
    
    #paper_1 = Paper(AuthorID=1, FileName="paper one", Title="paper title")
    
    # reviewerID = Reviewer.query.all()[0].ReviewerID
    # print(reviewerID)

    
    # papers = Paper.query.all()
    # for paper in papers:
    #     print(paper.PaperID)
    # review_1 = Review(PaperID=1, ReviewerID=1)
    # review_2 = Review(PaperID=2, ReviewerID=1)
    # review_3 = Review(PaperID=3, ReviewerID=1)

    # db.session.add(review_1)
    # db.session.add(review_2)
    # db.session.add(review_3)

    # db.session.commit()

    print(Review.query.all())

    
    
    #print(Paper.query.all())
    


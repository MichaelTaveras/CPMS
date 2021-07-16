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
# @login_required -> cant access page unless user logged in

app = Blueprint('app', __name__)

# user login page
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
                 login_user(author, remember=False)
                 return redirect(url_for('app.index'))
            else:
                 flash('Wrong password. Please try again.', category='error')
        elif reviewer:
            if check_password_hash(reviewer.Password, password):
                 flash('You have been successfully logged in.', category='succes')
                 login_user(reviewer, remember=False)
                 return redirect(url_for('app.index'))
            else:
                 flash('Wrong password. Please try again.', category='error')
        else:
            flash('Email does not exist.  Please try again.', category='error')

    return render_template('LoginForm.html')

# forgot password page
@app.route('/Forgot')
def Forgot():
    return render_template('Forgot.html')

# user registration page
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

        topic = request.form.getlist('Topics')
        
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
                aa = False
                app = False
                arc = False
                ai = False
                ce = False
                curr = False
                dst = False
                dab = False
                dl = False
                dsy = False
                esi = False
                fyc = False
                gi = False 
                gw = False 
                gip = False
                hci = False
                labe = False
                lit = False
                mic = False
                mm = False
                ndc = False
                nmc = False
                ooi = False
                ops = False
                pp = False
                pgg = False
                plg = False
                rsc = False
                sec = False
                swe = False
                sad = False
                tec = False
                wip = False
                oth = False

                topics = request.form.getlist('topics')
                for topic in topics:
                    if topic == "AA":
                        aa = True
                    elif topic == "APP":
                        app = True
                    elif topic == "ARC":
                        arc = True
                    elif topic == "AI":
                        ai = True
                    elif topic == "CE":    
                        ce = True
                    elif topic == "CURR":
                        curr = True
                    elif topic == "DST":
                        dst = True
                    elif topic == "DB":
                        dab = True
                    elif topic == "DL":
                        dl = True
                    elif topic == "DSY":
                        dsy = True
                    elif topic == "ESI":
                        esi = True
                    elif topic == "FYC":
                        fyc = True
                    elif topic == "GI":
                        gi = True
                    elif topic == "GW":
                        gw = True
                    elif topic == "GIP":
                        gip = True
                    elif topic == "HCI":
                        hci = True
                    elif topic == "LE":
                        labe = True
                    elif topic == "LIT":
                        lit = True
                    elif topic == "MIC":
                        mic = True
                    elif topic == "MM":
                        mm = True
                    elif topic == "NDC":
                        ndc = True
                    elif topic == "NMC":
                        nmc = True
                    elif topic == "OOI":
                        ooi = True
                    elif topic == "OS":
                        ops = True
                    elif topic == "PP":
                        pp = True
                    elif topic == "PGG":
                        pgg = True
                    elif topic == "PLG":
                        plg = True
                    elif topic == "RSC":
                        rsc = True
                    elif topic == "SEC":
                        sec = True
                    elif topic == "SWE":
                        swe = True
                    elif topic == "SAD":
                        sad = True
                    elif topic == "TEC":
                        tec = True
                    elif topic == "WIP":
                        wip = True
                    elif topic == "OTH":
                        oth  = True 

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
                    Password = generate_password_hash(password, method='sha256'),
                    AnalysisOfAlgorithms = aa,
                    Applications = app,
                    Architecture = arc,
                    ArtificialIntelligence = ai,
                    ComputerEngineering = ce,
                    Curriculum = curr,
                    DataStructures = dst,
                    Databases = dab,
                    DistanceLearning = dl,
                    DistributedSystems = dsy,
                    EthicalSocietalIssues = esi,
                    FirstYearComputing = fyc,
                    GenderIssues = gi,
                    GrantWriting = gw,
                    GraphicsImageProcessing = gip,
                    HumanComputerInteration = hci,
                    LaboratoryEnvironments = labe,
                    Literacy = lit,
                    MathematicsinComputing = mic,
                    Multimedia = mm,
                    NetworkingDataCommunications = ndc,
                    NonMajorCourses= nmc,
                    ObjectOrientedIssues = ooi,
                    OperatingSystems = ops,
                    ParallelProcessing = pp,
                    Pedagogy = pgg,
                    ProgrammingLanguages = plg,
                    Research = rsc,
                    Security = sec,
                    SoftwareEngineering = swe,
                    SystemsAnalysisandDesign = sad,
                    UsingTechnologyintheClassroom = tec,
                    WebandInternetProgramming = wip,
                    Other = oth)
                    
            else:
                print("Error on user type")

            # to database
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=False)
            flash('Account created!', category='success')

            return redirect(url_for('app.index'))
            

    return render_template('RegistrationForm.html', user=current_user)

# paper submition page
@app.route('/paperSubmitForm', methods=['GET', 'POST'])
@login_required
def paperSubmitForm():
    if request.method == 'POST':
        title = request.form.get('Title')
        file = request.files['File']
        fileName = file.filename

        aa = False
        app = False
        arc = False
        ai = False
        ce = False
        curr = False
        dst = False
        dab = False
        dl = False
        dsy = False
        esi = False
        fyc = False
        gi = False 
        gw = False 
        gip = False
        hci = False
        labe = False
        lit = False
        mic = False
        mm = False
        ndc = False
        nmc = False
        ooi = False
        ops = False
        pp = False
        pgg = False
        plg = False
        rsc = False
        sec = False
        swe = False
        sad = False
        tec = False
        wip = False
        oth = False


        topics = request.form.getlist('topics')
        for topic in topics:
            if topic == "AA":
                aa = True
            elif topic == "APP":
                app = True
            elif topic == "ARC":
                arc = True
            elif topic == "AI":
                ai = True
            elif topic == "CE":    
                ce = True
            elif topic == "CURR":
                curr = True
            elif topic == "DST":
                dst = True
            elif topic == "DB":
                dab = True
            elif topic == "DL":
                dl = True
            elif topic == "DSY":
                dsy = True
            elif topic == "ESI":
                esi = True
            elif topic == "FYC":
                fyc = True
            elif topic == "GI":
                gi = True
            elif topic == "GW":
                gw = True
            elif topic == "GIP":
                gip = True
            elif topic == "HCI":
                hci = True
            elif topic == "LE":
                labe = True
            elif topic == "LIT":
                lit = True
            elif topic == "MIC":
                mic = True
            elif topic == "MM":
                mm = True
            elif topic == "NDC":
                ndc = True
            elif topic == "NMC":
                nmc = True
            elif topic == "OOI":
                ooi = True
            elif topic == "OS":
                ops = True
            elif topic == "PP":
                pp = True
            elif topic == "PGG":
                pgg = True
            elif topic == "PLG":
                plg = True
            elif topic == "RSC":
                rsc = True
            elif topic == "SEC":
                sec = True
            elif topic == "SWE":
                swe = True
            elif topic == "SAD":
                sad = True
            elif topic == "TEC":
                tec = True
            elif topic == "WIP":
                wip = True
            elif topic == "OTH":
                oth  = True 


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
                AnalysisOfAlgorithms = aa,
                Applications = app,
                Architecture = arc,
                ArtificialIntelligence = ai,
                ComputerEngineering = ce,
                Curriculum = curr,
                DataStructures = dst,
                Databases = dab,
                DistanceLearning = dl,
                DistributedSystems = dsy,
                EthicalSocietalIssues = esi,
                FirstYearComputing = fyc,
                GenderIssues = gi,
                GrantWriting = gw,
                GraphicsImageProcessing = gip,
                HumanComputerInteration = hci,
                LaboratoryEnvironments = labe,
                Literacy = lit,
                MathematicsinComputing = mic,
                Multimedia = mm,
                NetworkingDataCommunications = ndc,
                NonMajorCourses= nmc,
                ObjectOrientedIssues = ooi,
                OperatingSystems = ops,
                ParallelProcessing = pp,
                Pedagogy = pgg,
                ProgrammingLanguages = plg,
                Research = rsc,
                Security = sec,
                SoftwareEngineering = swe,
                SystemsAnalysisandDesign = sad,
                UsingTechnologyintheClassroom = tec,
                WebandInternetProgramming = wip,
                Other = oth,
                )

            
            db.session.add(new_paper)
            db.session.commit()
            flash('Paper Submitted!', category='success')
            return redirect(url_for('app.index'))





    return render_template('paperSubmitForm.html',user=current_user)


# user home page
@app.route('/', methods=['GET', 'POST'])
@login_required 
def index():
    # have correct things show depending on user
   
    author = Author.query.filter_by(EmailAddress=current_user.EmailAddress).first()
    reviewer = Reviewer.query.filter_by(EmailAddress=current_user.EmailAddress).first()
  
    if author:
        userType = 'author'
    elif reviewer:
        userType = 'reviewer'

    return render_template('PaperPage.html', user=current_user, userType=userType)

# user account settings
@app.route('/AccountSettings',methods=['GET','POST'])
@login_required
def AccountSettings():
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

        topic = request.form.getlist('Topics')
        
        author = Author.query.filter_by(EmailAddress=email).first()
        reviewer = Reviewer.query.filter_by(EmailAddress=email).first()

        if len(email) < 5:
            flash('Email must be greater than 5 characters.', category='error')
        elif len(password) != 5:
            flash('Password must be 5 characters.', category='error')
        else:
            if userType == 'author':
                author.FirstName = fname,
                author.MiddleInitial = midIn,
                author.LastName = lname,
                author.Affiliation = affil,
                author.Department = dep,
                author.Address = address,
                author.City = city,
                author.State = state,
                author.ZipCode = zip,
                author.EmailAddress = email,
                author.PhoneNumber = phone,

            elif userType == 'reviewer':
                reviewer.FirstName = fname,
                reviewer.MiddleInitial = midIn,
                reviewer.LastName = lname,
                reviewer.Affiliation = affil,
                reviewer.Department = dep,
                reviewer.Address = address,
                reviewer.City = city,
                reviewer.State = state,
                reviewer.ZipCode = zip,
                reviewer.EmailAddress = email,
                reviewer.PhoneNumber = phone,
                # 
            else:
                print("Error on user type")


            # to database
            db.session.commit()
            flash('Account Updated!', category='success')

            return redirect(url_for('app.index'))
            
    
    return render_template('AccountSettings.html', user=current_user)


@app.route('/authorViewForm')
@login_required
def authorViewForm():

    return render_template('authorViewForm.html',user=current_user)

# user log out functionality
@app.route('/logout')
@login_required #cant access page unless user logged in
def LogOut():
    logout_user()
    return redirect(url_for('app.LoginForm'))


# admin page
@app.route('/Management', methods=['GET'])
@login_required
def Management():
    print("all authors")
    authors = get_authors()
    reviewers = get_reviewers()
    reviews = get_reviews()
    papers = get_papers()
    
    return render_template('Management.html',user=current_user, authors=authors, reviewers=reviewers, reviews=reviews, papers=papers)

# admin author info edit
@app.route('/manage_author', methods=['GET', 'POST','DELETE'])
def manage_author(x=None, y=None):
    authorID = request.args.get("AuthorID")
    if "delete" in request.form:
        author = Author.query.filter_by(AuthorID=authorID).first()
        db.session.delete(author)
        db.session.commit()
    elif "edit" in request.form:
        print(f"edit got called for {authorID}")
    
    return redirect("Management", code=200)

@app.route('/manage_reviewer', methods=['GET', 'POST','DELETE'])
def manage_reviewer(x=None, y=None):
    reviewerID = request.args.get("ReviewerID")
    if "delete" in request.form:
        reviewer = Reviewer.query.filter_by(ReviewerID=reviewerID).first()
        db.session.delete(reviewer)
        db.session.commit()
    elif "edit" in request.form:
        print(f"edit got called for {reviewerID}")
    
    return redirect("Management", code=200)

@app.route('/manage_review', methods=['GET', 'POST','DELETE'])
def manage_review(x=None, y=None):
    reviewID = request.args.get("ReviewID")
    if "delete" in request.form:
        review = Review.query.filter_by(ReviewID=reviewID).first()
        db.session.delete(review)
        db.session.commit()
    elif "edit" in request.form:
        print(f"edit got called for {reviewID}")
    
    return redirect("Management", code=200)

@app.route('/manage_paper', methods=['GET', 'POST','DELETE'])
def manage_paper(x=None, y=None):
    paperID = request.args.get("PaperID")
    if "delete" in request.form:
        paper = Paper.query.filter_by(PaperID=paperID).first()
        db.session.delete(paper)
        db.session.commit()
    elif "edit" in request.form:
        print(f"edit got called for {paperID}")
    
    return redirect("Management", code=200)

# admin paper to review page
@app.route('/PaperReview')
@login_required
def PaperReview():
    reviews = get_reviews()
    reviewers = get_reviewers()
    
    paper_ids = {}
    reviewer_ids = {}
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

# allows user to choose view
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
    author = Author.query.filter_by(EmailAddress=current_user.EmailAddress).first()
    reviewer = Reviewer.query.filter_by(EmailAddress=current_user.EmailAddress).first()
  
    if author:
        userType = 'author'
    elif reviewer:
        userType = 'reviewer'

    return render_template('viewForm.html',user=current_user, userType=userType)

# review submition form
@app.route('/ReviewForm', methods=['GET','POST'])
@login_required
def ReviewForm():
    if request.method == 'POST':
            userType = request.form.get('type')

            fname = request.form.get('FirstName')
            midIn = request.form.get('MiddleInitial')
            lname = request.form.get('LastName')

            PaperT = request.form.get('PaperTitle')#Paper title

            
            paper = Paper.query.filter_by(Title=PaperT).first()
            
            ApproTopic = request.form.get('AoT')
            TimeliTopic = request.form.get('ToT')
            SupportiveEvi = request.form.get('SE')
            TechQual = request.form.get('TQ')
            ScopeCov = request.form.get('SoC')
            CitationPrevWork = request.form.get('CPV')
            Original = request.form.get('Orig')
            ConCom = request.form.get('CC')
            
            OrganPaper = request.form.get('OoP')
            ClarityMess = request.form.get('CMM')
            Mechanics = request.form.get('mech')
            WrittenCom = request.form.get('WDC')
            
            
            SuitPres = request.form.get('SfP')
            PotIntTop = request.form.get('PIT')
            PotOralCom = request.form.get('POPC')
            
            OverallRate = request.form.get('OverRate')
            OverCom = request.form.get('ORC')
        
            newReview = Review(
            # PaperID = paper.PaperID,
            ReviewerID=current_user.ReviewerID, 
            ApproTopic = ApproTopic,
            TimeliTopic = TimeliTopic,
            SupportiveEvi = SupportiveEvi,
            TechQual = TechQual,
            ScopeCov = ScopeCov,
            CitationPrevWork = CitationPrevWork,
            Original = Original,
            ConCom = ConCom,
            
            OrganPaper = OrganPaper,
            ClarityMess = ClarityMess,
            Mechanics = Mechanics,
            WrittenCom = WrittenCom,
            
            SuitPres = SuitPres,
            PotIntTop = PotIntTop,
            PotOralCom = PotOralCom,
            
            OverallRate = OverallRate,
            OverCom = OverCom
            )

        # to database
            db.session.add(newReview)#make new review variable
            db.session.commit()

            flash('Review Submitted', category='success')
            return redirect(url_for('app.index'))
    return render_template('ReviewForm.html', user=current_user)

# @app.route('/PaperPage', methods=['GET', 'POST'])
# @login_required
# def PaperPage():
#     papers = get_papers()
#     return render_template('PaperPage.html',user=current_user, papers=papers)

# allows for fake up to db
def fake_upload():
    paper_1 = Paper(AuthorID=1, FileName="paper one", Title="paper title")
    
    reviewerID = Reviewer.query.all()[0].ReviewerID
    print(reviewerID)

    
    papers = Paper.query.all()
    for paper in papers:
        print(paper.PaperID)
    review_1 = Review(PaperID=1, ReviewerID=1)
    review_2 = Review(PaperID=2, ReviewerID=1)
    review_3 = Review(PaperID=3, ReviewerID=1)

    db.session.add(review_1)
    db.session.add(review_2)
    db.session.add(review_3)

    db.session.commit()

    print(Review.query.all())

    
    
    #print(Paper.query.all())

# returns all authors
def get_authors():
    return Author.query.all()
    
# returns all authors   
def get_reviewers():
    return Reviewer.query.all()

# returns all reviews
def get_reviews():
    return Review.query.all()

# returns all papers
def get_papers():
    return Paper.query.all()

# TODO:
# account settings update
# link papers to review
# review form page access


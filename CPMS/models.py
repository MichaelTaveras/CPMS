from enum import unique
from . import db
from flask_login import UserMixin
# from sqlalchemy.sql import func

# model for author
class Author(db.Model, UserMixin):
    # __tablename__ = 'author'

    AuthorID        = db.Column(db.Integer, primary_key=True,)
    FirstName       = db.Column(db.String(50))
    MiddleInitial   = db.Column(db.String(1))
    LastName        = db.Column(db.String(50))
    Affiliation     = db.Column(db.String(50))
    Department      = db.Column(db.String(50))
    Address         = db.Column(db.String(50))
    City            = db.Column(db.String(50))
    State           = db.Column(db.String(2))
    ZipCode         = db.Column(db.String(10))
    PhoneNumber     = db.Column(db.String(50))
    EmailAddress    = db.Column(db.String(100),unique=True)
    Password        = db.Column(db.String(5))
    Papers          = db.relationship('Paper')

    # uses authorID for getting ID
    def get_id(self):
        return self.AuthorID

# model for reviewers
class Reviewer(db.Model, UserMixin):
    # __tablename__ = 'reviewer'

    ReviewerID      = db.Column(db.Integer, primary_key=True)
    FirstName       = db.Column(db.String(50))
    MiddleInitial   = db.Column(db.String(1))
    LastName        = db.Column(db.String(50))
    Affiliation     = db.Column(db.String(50))
    Department      = db.Column(db.String(50))
    Address         = db.Column(db.String(50))
    City            = db.Column(db.String(50))
    State           = db.Column(db.String(2))
    ZipCode         = db.Column(db.String(10))
    PhoneNumber     = db.Column(db.String(50))
    EmailAddress    = db.Column(db.String(100), unique=True)
    Password        = db.Column(db.String(5))
    Reviews         = db.relationship('Review')
    AnalysisOfAlgorithms = db.Column(db.LargeBinary(1))
    Applications = db.Column(db.LargeBinary(1))
    Architecture = db.Column(db.LargeBinary(1))
    ArtificialIntelligence = db.Column(db.LargeBinary(1))
    ComputerEngineering = db.Column(db.LargeBinary(1))
    Curriculum = db.Column(db.LargeBinary(1))
    DataStructures = db.Column(db.LargeBinary(1))
    Databases = db.Column(db.LargeBinary(1))
    DistanceLearning = db.Column(db.LargeBinary(1))
    DistributedSystems = db.Column(db.LargeBinary(1))
    EthicalSocietalIssues = db.Column(db.LargeBinary(1))
    FirstYearComputing = db.Column(db.LargeBinary(1))
    GenderIssues = db.Column(db.LargeBinary(1))
    GrantWriting = db.Column(db.LargeBinary(1))
    GraphicsImageProcessing = db.Column(db.LargeBinary(1))
    HumanComputerInteration = db.Column(db.LargeBinary(1))
    LaboratoryEnvironments = db.Column(db.LargeBinary(1))
    Literacy = db.Column(db.LargeBinary(1))
    MathematicsinComputing = db.Column(db.LargeBinary(1))
    Multimedia = db.Column(db.LargeBinary(1))
    NetworkingDataCommunications = db.Column(db.LargeBinary(1))
    NonMajorCourses = db.Column(db.LargeBinary(1))
    ObjectOrientedIssues = db.Column(db.LargeBinary(1))
    OperatingSystems = db.Column(db.LargeBinary(1))
    ParallelProcessing = db.Column(db.LargeBinary(1))
    Pedagogy = db.Column(db.LargeBinary(1))
    ProgrammingLanguages = db.Column(db.LargeBinary(1))
    Research = db.Column(db.LargeBinary(1))
    Security = db.Column(db.LargeBinary(1))
    SoftwareEngineering = db.Column(db.LargeBinary(1))
    SystemsAnalysisandDesign = db.Column(db.LargeBinary(1))
    UsingTechnologyintheClassroom = db.Column(db.LargeBinary(1))
    WebandInternetProgramming = db.Column(db.LargeBinary(1))
    Other = db.Column(db.LargeBinary(1))

     # uses reviewerID for getting ID
    def get_id(self):
        return self.ReviewerID


# model for papers
class Paper(db.Model,UserMixin):
    # __tablename__ = 'paper'

    PaperID       = db.Column(db.Integer, primary_key=True)
    AuthorID      = db.Column(db.Integer, db.ForeignKey('author.AuthorID'))
    Active        = db.Column(db.LargeBinary(1))
    FileName      = db.Column(db.String(100))
    FileData      = db.Column(db.LargeBinary)
    Title         = db.Column(db.String(500))
    Certification = db.Column(db.String(3))
    AnalysisOfAlgorithms = db.Column(db.LargeBinary(1))
    Applications = db.Column(db.LargeBinary(1))
    Architecture = db.Column(db.LargeBinary(1))
    ArtificialIntelligence = db.Column(db.LargeBinary(1))
    ComputerEngineering = db.Column(db.LargeBinary(1))
    Curriculum = db.Column(db.LargeBinary(1))
    DataStructures = db.Column(db.LargeBinary(1))
    Databases = db.Column(db.LargeBinary(1))
    DistanceLearning = db.Column(db.LargeBinary(1))
    DistributedSystems = db.Column(db.LargeBinary(1))
    EthicalSocietalIssues = db.Column(db.LargeBinary(1))
    FirstYearComputing = db.Column(db.LargeBinary(1))
    GenderIssues = db.Column(db.LargeBinary(1))
    GrantWriting = db.Column(db.LargeBinary(1))
    GraphicsImageProcessing = db.Column(db.LargeBinary(1))
    HumanComputerInteration = db.Column(db.LargeBinary(1))
    LaboratoryEnvironments = db.Column(db.LargeBinary(1))
    Literacy = db.Column(db.LargeBinary(1))
    MathematicsinComputing = db.Column(db.LargeBinary(1))
    Multimedia = db.Column(db.LargeBinary(1))
    NetworkingDataCommunications = db.Column(db.LargeBinary(1))
    NonMajorCourses = db.Column(db.LargeBinary(1))
    ObjectOrientedIssues = db.Column(db.LargeBinary(1))
    OperatingSystems = db.Column(db.LargeBinary(1))
    ParallelProcessing = db.Column(db.LargeBinary(1))
    Pedagogy = db.Column(db.LargeBinary(1))
    ProgrammingLanguages = db.Column(db.LargeBinary(1))
    Research = db.Column(db.LargeBinary(1))
    Security = db.Column(db.LargeBinary(1))
    SoftwareEngineering = db.Column(db.LargeBinary(1))
    SystemsAnalysisandDesign = db.Column(db.LargeBinary(1))
    UsingTechnologyintheClassroom = db.Column(db.LargeBinary(1))
    WebandInternetProgramming = db.Column(db.LargeBinary(1))
    Other = db.Column(db.LargeBinary(1))


# model for reviews
class Review(db.Model,UserMixin):
    # __tablename__ = 'review'

    ReviewID      = db.Column(db.Integer, primary_key=True)
    PaperID       = db.Column(db.Integer, db.ForeignKey('paper.PaperID'))
    ReviewerID    = db.Column(db.Integer, db.ForeignKey('reviewer.ReviewerID'))
    # columns for Review ratings

    pass


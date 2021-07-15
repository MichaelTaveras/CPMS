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
    AnalysisOfAlgorithms = db.Column(db.Boolean)
    Applications = db.Column(db.Boolean)
    Architecture = db.Column(db.Boolean)
    ArtificialIntelligence = db.Column(db.Boolean)
    ComputerEngineering = db.Column(db.Boolean)
    Curriculum = db.Column(db.Boolean)
    DataStructures = db.Column(db.Boolean)
    Databases = db.Column(db.Boolean)
    DistanceLearning = db.Column(db.Boolean)
    DistributedSystems = db.Column(db.Boolean)
    EthicalSocietalIssues = db.Column(db.Boolean)
    FirstYearComputing = db.Column(db.Boolean)
    GenderIssues = db.Column(db.Boolean)
    GrantWriting = db.Column(db.Boolean)
    GraphicsImageProcessing = db.Column(db.Boolean)
    HumanComputerInteration = db.Column(db.Boolean)
    LaboratoryEnvironments = db.Column(db.Boolean)
    Literacy = db.Column(db.Boolean)
    MathematicsinComputing = db.Column(db.Boolean)
    Multimedia = db.Column(db.Boolean)
    NetworkingDataCommunications = db.Column(db.Boolean)
    NonMajorCourses = db.Column(db.Boolean)
    ObjectOrientedIssues = db.Column(db.Boolean)
    OperatingSystems = db.Column(db.Boolean)
    ParallelProcessing = db.Column(db.Boolean)
    Pedagogy = db.Column(db.Boolean)
    ProgrammingLanguages = db.Column(db.Boolean)
    Research = db.Column(db.Boolean)
    Security = db.Column(db.Boolean)
    SoftwareEngineering = db.Column(db.Boolean)
    SystemsAnalysisandDesign = db.Column(db.Boolean)
    UsingTechnologyintheClassroom = db.Column(db.Boolean)
    WebandInternetProgramming = db.Column(db.Boolean)

     # uses reviewerID for getting ID
    def get_id(self):
        return self.ReviewerID


# model for papers
class Paper(db.Model,UserMixin):
    # __tablename__ = 'paper'

    PaperID       = db.Column(db.Integer, primary_key=True)
    AuthorID      = db.Column(db.Integer, db.ForeignKey('author.AuthorID'))
    Active        = db.Column(db.Boolean)
    FileName      = db.Column(db.String(100))
    FileData      = db.Column(db.LargeBinary)
    Title         = db.Column(db.String(500))
    Certification = db.Column(db.String(3))

    AnalysisOfAlgorithms = db.Column(db.Boolean)
    Applications = db.Column(db.Boolean)
    Architecture = db.Column(db.Boolean)
    ArtificialIntelligence = db.Column(db.Boolean)
    ComputerEngineering = db.Column(db.Boolean)
    Curriculum = db.Column(db.Boolean)
    DataStructures = db.Column(db.Boolean)
    Databases = db.Column(db.Boolean)
    DistanceLearning = db.Column(db.Boolean)
    DistributedSystems = db.Column(db.Boolean)
    EthicalSocietalIssues = db.Column(db.Boolean)
    FirstYearComputing = db.Column(db.Boolean)
    GenderIssues = db.Column(db.Boolean)
    GrantWriting = db.Column(db.Boolean)
    GraphicsImageProcessing = db.Column(db.Boolean)
    HumanComputerInteration = db.Column(db.Boolean)
    LaboratoryEnvironments = db.Column(db.Boolean)
    Literacy = db.Column(db.Boolean)
    MathematicsinComputing = db.Column(db.Boolean)
    Multimedia = db.Column(db.Boolean)
    NetworkingDataCommunications = db.Column(db.Boolean)
    NonMajorCourses = db.Column(db.Boolean)
    ObjectOrientedIssues = db.Column(db.Boolean)
    OperatingSystems = db.Column(db.Boolean)
    ParallelProcessing = db.Column(db.Boolean)
    Pedagogy = db.Column(db.Boolean)
    ProgrammingLanguages = db.Column(db.Boolean)
    Research = db.Column(db.Boolean)
    Security = db.Column(db.Boolean)
    SoftwareEngineering = db.Column(db.Boolean)
    SystemsAnalysisandDesign = db.Column(db.Boolean)
    UsingTechnologyintheClassroom = db.Column(db.Boolean)
    WebandInternetProgramming = db.Column(db.Boolean)


    def getActiveTopics(self):
        topicList =  [
    self.AnalysisOfAlgorithms,
    self.Applications,
    self.Architecture,
    self.ArtificialIntelligence,
    self.ComputerEngineering,
    self.Curriculum,
    self.DataStructures,
    self.Databases,
    self.DistanceLearning,
    self.DistributedSystems,
    self.EthicalSocietalIssues,
    self.FirstYearComputing,
    self.GenderIssues,
    self.GrantWriting,
    self.GraphicsImageProcessing,
    self.HumanComputerInteration,
    self.LaboratoryEnvironments,
    self.Literacy,
    self.MathematicsinComputing,
    self.Multimedia,
    self.NetworkingDataCommunications,
    self.NonMajorCourses,
    self.ObjectOrientedIssues,
    self.OperatingSystems,
    self.ParallelProcessing,
    self.Pedagogy,
    self.ProgrammingLanguages,
    self.Research,
    self.Security,
    self.SoftwareEngineering,
    self.SystemsAnalysisandDesign,
    self.UsingTechnologyintheClassroom,
    self.WebandInternetProgramming]

        return [ x for x in topicList if x ==True]


# model for reviews
class Review(db.Model,UserMixin):
    # __tablename__ = 'review'

    ReviewID      = db.Column(db.Integer, primary_key=True)
    PaperID       = db.Column(db.Integer, db.ForeignKey('paper.PaperID'))
    ReviewerID    = db.Column(db.Integer, db.ForeignKey('reviewer.ReviewerID'))
    # columns for Review ratings

    pass


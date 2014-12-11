#GAE Imports
from google.appengine.ext import db

class Course( db.Model ) :

    CourseName = db.StringProperty( required = True )
    CourseNum = db.StringProperty( required = True )

    CourseInstr = db.UserProperty( required = True )
    CourseCoInstr = db.StringProperty()

    Credits = db.IntegerProperty( required = True )
    ClassTimings = db.TextProperty()
    Location = db.StringProperty()

    NumLectures = db.IntegerProperty()
    OfficeHours = db.StringProperty()
    Website = db.LinkProperty()

    MailingList = db.EmailProperty()
    TextBook = db.StringProperty()

    CourseStructure = db.TextProperty()
    GradingPolicy = db.TextProperty()
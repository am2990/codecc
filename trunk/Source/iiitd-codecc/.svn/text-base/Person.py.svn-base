#GAE Imports
from google.appengine.ext import db

class Person( db.Model ) :

    USER = db.UserProperty( required = True )

    Prefix = db.StringProperty()
    FirstName = db.StringProperty( required = True )
    LastName = db.StringProperty()

    Email = db.EmailProperty( required = True )
    Contact = db.PhoneNumberProperty( required = True )

    Profile = db.TextProperty()
    Picture = db.BlobProperty()


#Checks if a user exists in the system
#If yes, return the PERSON instance else returns None
def UserExists( User ) :

    UserCheck = Person.all()
    UserCheck.filter("USER = ",User)

    PERSON = UserCheck.get()

    if( PERSON != None ): return PERSON

    else: return None
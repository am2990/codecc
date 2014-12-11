#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#Python Standard Lib Imports
import os

#GAE Imports
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import util
from google.appengine.api import users

#Application Imports
import Person
import Course

#Serves Images
class ImageRenderer( webapp.RequestHandler ):

    def get(self):

      PERSON = db.get( self.request.get("entity") )
      #self.response.out.write(PERSON.Picture)
      
      if PERSON.Picture :
          self.response.headers['Content-Type'] = "image/jpg"
          self.response.out.write(PERSON.Picture)
      
      else:    
          self.redirect("images/defaultprofile.png")

class AddNewCourseHandler( webapp.RequestHandler ) :

    def get(self):
        User = users.get_current_user()
        if User:
            CourseNum = self.request.get('CourseNum')
            template_values = {
                'semester': "MONSOON SEMESTER",
                'firstname': User.nickname(),
                'lastname': "",
                'email': " ("+User.email()+")",
                'info':'',
                'image': "",
                'courses':[],
                'menu':[["",""]],
                'logout_url': users.create_logout_url("/"),
                'CourseNum': CourseNum
                                  }
    
            path = os.path.join( os.path.dirname(__file__) , 'WebUI/templates/courses/AddNewCourse.html' )
            self.response.out.write( template.render( path , template_values ) )
        else:
            self.redirect("/")

class AddNewCourseFrameHandler( webapp.RequestHandler ) :

    def get(self):
        User = users.get_current_user()
        if User:
            CourseNum = self.request.get('CourseNum')
            template_values = {
                                "CourseNum":CourseNum
                              }
            path = os.path.join( os.path.dirname(__file__) , 'WebUI/templates/courses/course_structure.html' )
            self.response.out.write( template.render( path , template_values ) )
        else:
            self.redirect("/")
        



#Entry point for the web-application, Uses GAE User API for authentication
class LoginHandler( webapp.RequestHandler ) :

    def get(self) :
                
        User = users.get_current_user() #Get the current logged in user object

        #If user is authenticated
        if User:
            template_values = {
                'semester': "MONSOON SEMESTER",
                'firstname': User.nickname(),
                'lastname': "",
                'email': " ("+User.email()+")",
                'info':'',
                'image': "",
                'courses':[],
                'menu':[["",""]],
                'logout_url': users.create_logout_url("/")
                                  }
        
            self.response.headers["Content-Type"] = "text/html"
            PERSON = Person.UserExists(User) #Retreive user entry from the datastore
            if( PERSON != None ) :
            
                template_values = {
                'semester': "MONSOON SEMESTER",
                'firstname': PERSON.Prefix+" "+PERSON.FirstName,
                'lastname': PERSON.LastName,
                'email': " ("+PERSON.Email+")",
                'info': PERSON.Prefix+" "+PERSON.FirstName+" "+PERSON.LastName+"<br><br>"+PERSON.Profile+"<br>"+PERSON.Contact,
                'image': 'img?entity='+str(PERSON.key()),
                'courses':[["1","MTH101","Basic Maths","Anshu Malhotra"],["2","SCI101","Basic Science","Vidushi"],["3","CSE101","Computer Science","N/A"]],
                'menu':[["Home","home.htm"],["Student","home.htm"],["TA","home.htm"]],
                'logout_url': users.create_logout_url("/"),
                                  }
            
                path = os.path.join( os.path.dirname(__file__) , 'WebUI/templates/faculty/faculty_courses_list.html' )
                self.response.out.write( template.render( path , template_values ) )

            else :
                template_values = {
                'semester': "MONSOON SEMESTER",
                'firstname': User.nickname(),
                'lastname': "",
                'email': " ("+User.email()+")",
                'info':'',
                'image': "",
                'courses':[],
                'menu':[["",""]],
                'logout_url': users.create_logout_url("/")
                                  }
               
                #Form for adding new user to the system
                self.response.out.write( template.render( 'WebUI/templates/User/NewUser.html' , template_values ) )
            
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." %
                        users.create_login_url("/"))
            self.response.out.write("<html><body>%s</body></html>" % greeting)


#Serves the New user creation Form
class NewUserFormHandler( webapp.RequestHandler ) :

    def get(self):
        
        User = users.get_current_user()

        if User :

            PERSON = Person.UserExists(User)
            if( PERSON != None ) :

                UserProfile = {
                'FirstName' : PERSON.FirstName,
                'LastName' : PERSON.LastName,
                'Email' : PERSON.Email,
                'CountryCode' : str(PERSON.Contact).split(" ")[0],
                'Contact' : str(PERSON.Contact).split(" ")[1],
                'Profile' : PERSON.Profile
                              }
                
                self.response.out.write( template.render( 'WebUI/templates/User/NewUserFrame.html' , UserProfile ) )

            else : 
                
                DefaultProfile = {
                'Profile' : "Enter a short description about yourself"
                                 }
                
                self.response.out.write( template.render( 'WebUI/templates/User/NewUserFrame.html' , DefaultProfile ) )
            

        else : self.redirect("/")    


#Handler for adding a new /editing an existing user to the system
class NewUserHandler( webapp.RequestHandler ) :

    #Receives data using 'POST' from the NewUserFrame.html form
    def post(self) :

        User = users.get_current_user()

        PERSON = Person.UserExists( User )
        if( PERSON != None ) :
            #Edit existing User
            PERSON.Prefix = self.request.get('Prefix')
            PERSON.FirstName = self.request.get('FirstName')
            PERSON.LastName = self.request.get('LastName')
            PERSON.Email = db.Email( self.request.get('Email') )
            PERSON.Contact = db.PhoneNumber( "(" + filter(lambda x: x.isdigit() , self.request.get('CountryCode')) + ") " +
                                            self.request.get('Contact') )
            PERSON.Profile = db.Text( self.request.get('Profile') )

        else :
            #Add the new User
            PERSON = Person( 
                             USER = users.get_current_user() ,
                             Prefix = self.request.get('Prefix'),
                             FirstName = self.request.get('FirstName'),
                             LastName = self.request.get('LastName'),
                             Email = db.Email( self.request.get('Email') ),
                             Contact = db.PhoneNumber( "(" + filter(lambda x: x.isdigit() , self.request.get('CountryCode')) + ") " +
                                                      self.request.get('Contact') ),
                             Profile = db.Text( self.request.get('Profile') ),
                           )

        ProfilePic = self.request.get('ProfilePic')

        if( ProfilePic != "" ) :
            PERSON.Picture = db.Blob( ProfilePic )
        
        PERSON.put()

        #Redirect to the home page
        self.redirect("/")


#Handler for editing user profile
class EditProfileHandler( webapp.RequestHandler ) :

    def get(self) :

        User = users.get_current_user()

        if User :
            
            template_values = {
            'semester': "MONSOON SEMESTER",
            'firstname': User.nickname(),
            'lastname': "",
            'email': " ("+User.email()+")",
            'info':'',
            'image': "",
            'courses':[],
            'menu':[["",""]],
            'logout_url': users.create_logout_url("/")
                              }
               
            #Form for adding new user to the system
            self.response.out.write( template.render( 'WebUI/templates/User/NewUser.html' , template_values ) )

        else : self.redirect("/")

    
def main():
    application = webapp.WSGIApplication([('/', LoginHandler),
                                          ('/img', ImageRenderer),
                                          ('/NewUser', NewUserFormHandler),
                                          ('/AddNewUser', NewUserHandler),
                                          ('/EditProfile', EditProfileHandler),
                                          ('/AddNewCourse', AddNewCourseHandler),
                                          ('/AddNewCourseFrame', AddNewCourseFrameHandler)],
                                         debug=True)

    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

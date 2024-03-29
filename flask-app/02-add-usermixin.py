pip install flask-login

from flask_login import UserMixin

A minxin is a acclass that gives some small in scope piece of functionality that is not standalone.


#Import the UserMixin from Flask-Login. 
#Remember that Flask extensions usually have import paths that start with flask.ext.
#Now add UserMixin to the inheritance chain of the User model.

import datetime

from flask_login import UserMixin
from peewee import *


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = TextField(default='')

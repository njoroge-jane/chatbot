from click import confirm
from flask import render_template,redirect,url_for,flash,request
from . import auth

from flask_login import login_user,logout_user,login_required
'''
add imports from forms here
'''
from ..models import user
from .. import db

user=user()

@auth.route('/login',methods=['GET','POST'])
def login():
  '''
  add login form route
  '''




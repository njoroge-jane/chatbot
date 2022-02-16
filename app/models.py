import decimal
from sqlalchemy import ForeignKey
from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return registration.query.get(int(user_id))
  

class registration(db.Model,UserMixin):
   __tablename__ = 'registration'

   id = db.Column(db.Integer,primary_key=True)
   contact = db.Column(db.String(255))
   username = db.Column(db.String(255))


   # userdetails = db.relationship('chat',backref='registration', lazy = 'dynamic')

   def __repr__(self):
     return f'(self.contact)'

class chat(db.Model):
   __tablename__ = 'chat'

   id = db.Column(db.Integer,primary_key=True)
   message_from = db.Column(db.String(100))
   message_to = db.Column(db.String(255))
   message = db.Column(db.String(3000))
   received_on = db.Column(db.DateTime, default=datetime.utcnow())

class pin(db.Model):
   __tablename__= 'pin'
   
   id = db.Column(db.Integer,primary_key=True) 
   user_pin = db.Column(db.ForeignKey('registration.id'))
   chat_pin = db.Column(db.Integer)
   

class contacts(db.Model):
   __tablename__ = 'contacts'
   id = db.Column(db.Integer, primary_key = True)
   added_by = db.Column(db.String(255))
   username = db.Column(db.String(255))
   contact = db.Column(db.String(100))
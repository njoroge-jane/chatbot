import decimal
from sqlalchemy import ForeignKey
from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.Integer)
    username = db.Column(db.String(255))

    pass_secure = db.Column(db.String(255))

   
    def __repr__(self):
        return f'(self.contact)'
        


class chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    message_from = db.Column(db.ForeignKey('user.id'))
    message_to = db.Column(db.String(255))
    message = db.Column(db.String(3000))
    received_on = db.Column(db.DateTime, default=datetime.utcnow())


class pin(db.Model):
    __tablename__ = 'pin'

    id = db.Column(db.Integer, primary_key=True)
    user_pin = db.Column(db.ForeignKey('user.id'))
    chat_pin = db.Column(db.Integer)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo
from app.models import users
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Enter username', validators=[InputRequired()])
    contact = StringField('Enter contact', validators=[InputRequired()])
    submit = SubmitField('Add contact')


class LoginForm(FlaskForm):
    username = StringField('Enter username', validators=[InputRequired()])
    contact = StringField('Enter contact', validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


def validate_username(self, username):
    user = users.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('Username already exists')


def validate_username(self, contact):
    user = users.query.filter_by(contact=contact.data).first()
    if user:
        raise ValidationError('That contact exists')

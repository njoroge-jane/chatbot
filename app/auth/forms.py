from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from app.models import user
from wtforms import ValidationError

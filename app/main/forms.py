from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,validators
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):

    contact = StringField('Contact',validators=[InputRequired()])
    username = StringField('Name',validators=[InputRequired()])
    submit = SubmitField('Save')

class PinForm(FlaskForm):
    new_pin = StringField('New Pin',[validators.InputRequired(),validators.EqualTo('confirm_pin', message='Passwords must match')])
    confirm_pin = StringField('Confirm Pin')
    submit = SubmitField('Submit')
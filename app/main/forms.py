from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):

    contact = StringField('Contact',validators=[InputRequired()])
    username = StringField('Name',validators=[InputRequired()])
    submit = SubmitField('Save')

class PinForm(FlaskForm):
    new_pin = StringField('New Pin')
    encrypt_pin = StringField('Encrypt Pin')
    submit = SubmitField('Submit')
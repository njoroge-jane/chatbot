from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):

    new_contact = StringField('Contact',validators=[InputRequired()])
    new_name = StringField('Name',validators=[InputRequired()])

    

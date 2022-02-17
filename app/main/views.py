from locale import format_string
from flask import flash, render_template, request, redirect, url_for, abort
from . import main
from ..models import user
from .. import db, photos
from flask_login import current_user, login_required
from ..models import user,chat,pin,contacts
from .forms import ContactForm, PinForm


@main.route('/index', methods = ['GET','POST'])
def index():

  contact_form = ContactForm()
  get_contact = contacts.query.filter_by(contact=contact_form.contact.data).first()
  if get_contact:
    flash('Contact Already exists!')

  else:

    if contact_form.validate_on_submit():
      contact = contacts(contact=contact_form.contact.data,
                          username=contact_form.username.data)
      
      db.session.add(contact)
      db.session.commit()

      flash('Contact successfully saved!')

    

  return render_template('new-contact.html', contact_form=contact_form)

@main.route('/', methods = ['GET','POST'])
def set_pin():

  pin_form = PinForm()
  
  if pin_form.validate_on_submit():

    first_pin = pin_form.new_pin.data
    second_pin = pin_form.confirm_pin.data

    get_pin = pin.query.filter_by(user_pin=current_user.id, chat_pin=second_pin).first()
    if get_pin:
      flash('The pin already exists')
      return redirect(request.referrer)
    else:
      new_pin=pin(user_pin=current_user.id, chat_pin=second_pin)
      db.session.add(new_pin)
      db.session.commit()
      return redirect(url_for('main.index'))
    
  return render_template('contact-pin.html', pin_form=pin_form)
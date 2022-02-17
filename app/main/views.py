from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import user
from .. import db, photos
from flask_login import login_required
from ..models import user,chat,pin
from .forms import ContactForm, PinForm


@main.route('/index', methods = ['GET','POST'])
def index():

  contact_form = ContactForm()

  return render_template('new-contact.html', contact_form=contact_form)

@main.route('/', methods = ['GET','POST'])
def pin():

  pin_form = PinForm()

  return render_template('contact-pin.html', pin_form=pin_form)
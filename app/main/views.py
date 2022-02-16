from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import user
from .. import db, photos
from flask_login import login_required
from ..models import user,chat,pin
from .forms import ContactForm


@main.route('/')
def index():

    form = ContactForm()

    return render_template('new-contact.html', contact_form=form)
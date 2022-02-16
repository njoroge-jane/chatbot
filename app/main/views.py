from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db, photos
from flask_login import login_user, current_user
from ..models import users, chat, pin


@main.route('/')
def home():
    return render_template('home.html', current_user=current_user.contact)

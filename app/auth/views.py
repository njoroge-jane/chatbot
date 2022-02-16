from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import users
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import current_user, login_user, logout_user, login_required


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    get_user = users.query.filter_by(contact=form.contact.data).first()
    if get_user:
        flash("User already exists")

    else:

        if form.validate_on_submit():
            user = users(username=form.username.data,
                         contact=form.contact.data)
            db.session.add(user)
            db.session.commit()

            flash('Account has been created successfully')

            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', registration_form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = users.query.filter_by(username=login_form.username.data).first()
        if (user.username == login_form.username.data):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid login details')
    title = "ChatBot login"
    return render_template('auth/login.html', login_form=login_form, title=title)

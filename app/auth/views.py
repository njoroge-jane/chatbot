from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import registration
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import current_user, login_user, logout_user, login_required


@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['saveusername']
        savecontact = request.form['savecontact']
        check_user = registration.query.filter_by(contact = savecontact , username = username).first()
        if check_user:
            flash("User with this username already exist")
            return redirect(request.referrer)
        else:
            new_user = registration(contact = savecontact ,username = username)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = registration.query.filter_by(username=login_form.username.data).first()
        if (user.username == login_form.username.data):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid login details')
    title = "ChatBot login"
    return render_template('auth/login.html', login_form=login_form, title=title)

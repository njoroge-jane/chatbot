from click import confirm
from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import user
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import current_user, login_user, logout_user, login_required

from app import app
'''
add imports from forms here
'''
from ..models import user
from .. import db

user = user()


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = user(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = user.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitch-App Login"
    return render_template('auth/login.html', login_form=login_form, title=title)

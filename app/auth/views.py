from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import users
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import current_user, login_user, logout_user, login_required


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = users(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form=form)

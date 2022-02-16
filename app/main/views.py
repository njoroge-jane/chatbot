from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db, photos
from flask_login import login_required
from ..models import users, chat, pin

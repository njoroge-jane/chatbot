from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import user
from .. import db, photos
from flask_login import login_required
from ..models import user,chat,pin
import base64


@main.route('/')
def index():
  title = "ChartBot"
  # mess = "RawlingsOtieno"
  # dec = base64.urlsafe_b64decode(mess)
  return render_template('index.html', title = title)

@main.route('/sendchart', methods = ['POST','GET'])
def sendchart():
  if request.method == 'POST':
    message = request.form['messages']
    # enc = message.encode('base64', 'strict')
    sender = current_user.id
    receiver = request.cookies.get('receiver')
    new_chart = chat(message_from = sender,message_to = receiver,message = message)

    db.session.add(new_chart)
    sent = db.commit()
    if sent:
      return redirect(request.refferer)
    else:
      flash("You cannot send message to this chart")
      return redirect(request.refferer)

@main.route('/recepient/<int:id>')
def recepient(id):
  setrecepient = set_cookie("receiver", id, max_age = 60 * 60)
  if setrecepient:
    return redirect(request.refferer)
  else:
    flash("This user is not registered with charbot")
    return redirect(request.refferer)


@main.route('/contact')
def contact():
  title = "Contact Form - Save Contact"
  return render_template('contact.html', title = title)

@main.route('/pin')
def pin():
  title = "Pin Form - Save Pin"
  return render_template('pin.html', title = title)
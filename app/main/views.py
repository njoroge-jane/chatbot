from flask import render_template, request, redirect, url_for, abort, flash, make_response
from . import main
from .forms import ContactForm,PinForm
from .. import db, photos
from flask_login import login_required, current_user
from ..models import registration,chat,pin,contacts
import base64


@main.route('/')
@login_required
def index():
  title = "ChartBot"
  curent = current_user.id
  froms = current_user.contact
  mainuserpref = current_user.username[0]
  names = request.cookies.get('receiver')
  # get current chart contact
  set_receiver = contacts.query.filter_by(contact = names).first()
  # get all contact
  get_contact = contacts.query.filter_by(added_by = froms).all()
  current_chats = chat.query.filter_by(message_to = current_user.contact).all()
  get_charts = chat.query.filter((chat.message_to == names ) & (chat.message_from == froms) | (chat.message_to == froms) & (chat.message_from == names))
  return render_template('index.html', set_receiver = set_receiver ,title = title, get_charts = get_charts, curent= curent, mainuserpref = mainuserpref, current_chats = current_chats, get_contact = get_contact, froms = froms)

@main.route('/sendchart', methods = ['POST','GET'])
def sendchart():
  if request.method == 'POST':
    message = request.form['messages']
    names = request.cookies.get('receiver')
    set_receiver = contacts.query.filter_by(contact = names).first()
    sender = str(current_user.contact)
    receiver = names
    new_chart = chat(message_from = sender,message_to = receiver,message = message)

    db.session.add(new_chart)
    sent = db.session.commit()
    if sent:
      return redirect(request.referrer)
    else:
      flash("You cannot send message to this chart")
      return redirect(request.referrer)

@main.route('/recepient/<int:id>')
def recepient(id):
  getcontact = contacts.query.filter_by(id = id).first()
  contactname = getcontact.contact
  resp = make_response(redirect('/'))
  setrecepient = resp.set_cookie("receiver", contactname)

  return resp


# @main.route('/contact')
# def contact():
#   title = "Contact Form - Save Contact"
#   return render_template('contact.html', title = title)

# @main.route('/pin')
# def pin():
#   title = "Pin Form - Save Pin"
#   return render_template('pin.html', title = title)

# @main.route('/addcontact', methods = ['POST', 'GET'])
# def addcontact():
#   if request.method == 'POST':
#     username = request.form['contactname']
#     contact = str(request.form['contactnumber'])
#     saveby = current_user.contact
#     get_contact = contacts.query.filter_by(added_by = saveby, contact = contact).first()
#     if get_contact:
#        flash("user with this contact already exist")
#        return redirect(request.referrer)
#     else:
#        new_contact = contacts(added_by = saveby,username = username,contact = contact)
#        db.session.add(new_contact)
#        db.session.commit()
#        return redirect(url_for('main.index'))


@main.route('/contact', methods = ['GET','POST'])
def contact():
    addedby = current_user.contact
    contact_form = ContactForm()
    get_contact = contacts.query.filter(contacts.added_by == addedby , contacts.contact == contact_form.contact.data).first()
    if get_contact:
      flash('Contact Already exists!')

    else:

      if contact_form.validate_on_submit():
        contact = contacts(added_by = addedby,username=contact_form.username.data, contact=contact_form.contact.data)
        
        db.session.add(contact)
        db.session.commit()

        flash('Contact successfully saved!')
        return redirect(url_for('main.index'))

    

    return render_template('contact.html', contact_form=contact_form)


@main.route('/pin', methods = ['GET','POST'])
def setpin():

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

  return render_template('pin.html', pin_form=pin_form)

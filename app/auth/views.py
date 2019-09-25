from flask import render_template,redirect,url_for,request,flash
from . import auth
from .forms import SignUpForm,LogInForm
from ..models import Writter
from .. import db
from flask_login import login_required,login_user

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
  form=SignUpForm()
  if form.validate_on_submit():
    writter = Writter(username=form.username.data,email=form.email.data, password=form.password.data)
    for field in form:
      if field == " ":
        flash(f"{field} is required")
        return render_template('signup.html')
    if form.password.data != form.confirm_password.data:
      flash("passwords dont match")
      return render_template("signup.html")
    name = writter.query.filter_by(username = writter.username).first()
    if name!=None:
      flash("user with that username exists")
      return render_template("signup.html")
    else:
      name = writter.query.filter_by(email = writter.email).first()
      if name != None:
        flash("user with that email exist")
        return render_template("signup.html")
      else:
        writter = Writter(username=form.username.data,email=form.email.data, password=form.password.data)
        writter.hash_password(form.password.data)
        db.session.add(writter)
        db.session.commit()
    return redirect(url_for('auth.login'))
  return render_template('signup.html',form=form)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
  logform=LogInForm()
  if logform.validate_on_submit():
    if logform.email.data == None or logform.password.data == None:
      flash("all fields habe to be filled")
    user = Writter.query.filter_by(email = Writter.email).first()
    if user != None:
      if user.check_password(logform.password.data) != False:
        login_user(user)
        return redirect(url_for('main.home'))
      else:
        flash("invalid username or password")
        return render_template("login.html",logform=logform)
    else:
      flash("invalid user")
      return redirect(url_for('auth.login'))
  return render_template('login.html',logform=logform)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))
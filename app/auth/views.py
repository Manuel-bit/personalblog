from flask import render_template,redirect,url_for,request
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
    db.session.add(writter)
    db.session.commit()
    return redirect(url_for('main.home'))
  return render_template('signup.html',form=form)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
  form=LogInForm()
  if form.validate_on_submit():
    writter= Writter.query.filter_by(email=form.email.data).first()
    if writter is not None and writter.verify_password(form.password.data):
      login_user(writter,form.remember.data)
      return redirect(url_for('main.home'))
      flash ('invalid email or password')


  return render_template('login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
  logout_writter()
  return redirect(url_for('main.index'))
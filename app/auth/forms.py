from wtforms import  StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,ValidationError,EqualTo
from ..models import Writter
from flask_wtf import FlaskForm 

class SignUpForm(FlaskForm):
  username=StringField("Username..", validators=[DataRequired()])
  email=StringField("Email..",validators=[DataRequired()])
  password=PasswordField("Enter Password",validators=[DataRequired()])
  confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
  submit=SubmitField("Sign Up")

class LogInForm(FlaskForm):
  email=StringField('Email',validators=[DataRequired()])
  password=PasswordField('password',validators=[DataRequired()])
  remember = BooleanField('Remember me')
  submit=SubmitField('Log in')



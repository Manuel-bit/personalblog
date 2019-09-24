from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class Blog(db.Model):
  __tablename__='blogs'
  id= db.Column(db.Integer,primary_key=True)
  blog= db.Column(db.String(500))
  author=db.Column(db.String(255))
  title=db.Column(db.String(255))
  blog_image=db.column(db.String(255))
  description= db.Column(db.String(255))
  comments=db.relationship('Comment',backref = 'blog',lazy='dynamic')
  writter_id=db.Column(db.Integer, db.ForeignKey('writters.id'))

  def __repr__(self):
    return f'User {self.username}'

class Comment(db.Model):
  __tablename__='comments'
  id=db.Column(db.Integer, primary_key=True)
  comment=db.Column(db.String(255))
  blog_id=db.Column(db.Integer, db.ForeignKey('blogs.id'))


class Writter(UserMixin,db.Model):
  __tablename__="writters"
  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(255))
  password=db.Column(db.String(255))
  email=db.Column(db.String(255),unique=True)
  blogs=db.relationship('Blog',backref = 'writter',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.password = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)


  @login_manager.user_loader
  def load_user(writter_id):
    return Writter.query.get(int(writter_id))
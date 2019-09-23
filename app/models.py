from . import db

class Blog(db.Model):
  __tablename__='blogs'
  id= db.Column(db.Integer,primary_key=True)
  blog= db.Column(db.String(500))
  author=db.Column(db.String(255))
  title=db.Column(db.String(255))
  blog_image=db.column(db.String(255))
  description= db.Column(db.String(255))
  comments=db.relationship('Comment',backref = 'blog',lazy='dynamic')

  def __repr__(self):
    return f'User {self.username}'

class Comment(db.Model):
  __tablename__='comments'
  id=db.Column(db.Integer, primary_key=True)
  comment=db.Column(db.Integer(255))
  blog_id=db.Column(db.Integer, db.Foreign_Key('blogs.id'))


class Writter(db.model):
  __tablename__="writters"
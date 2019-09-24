from flask import render_template,redirect,url_for,request
from . import main
from .forms import NewBlogForm
from ..models import Blog
from .. import db

@main.route('/home')
def home():

  blogs= Blog.query.all()
  return render_template('home.html',blogs=blogs)

@main.route('/newblog', methods =["GET", "POST"])
def newblog():
  form = NewBlogForm()
  if form.validate_on_submit():
    blog= Blog(title=form.title.data, author=form.author.data, description=form.description.data, blog=form.blog.data)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.home'))
  return render_template('newblog.html',form=form)

@main.route('/')
def index():
  
  return render_template('index.html')
from flask import render_template,redirect,url_for,request
from . import main
from .forms import NewBlogForm,AddComment
from ..models import Blog
from .. import db
from flask_login import login_required,current_user
from app.requests import fetchQuotes

@main.route('/')
def index():
  quote = fetchQuotes()

  return render_template('index.html',quote = quote)

@main.route('/home')
@login_required
def home():
  form=AddComment()
  blogs= Blog.query.all()
  return render_template('home.html',blogs=blogs,form=form)

@main.route('/newblog', methods =["GET", "POST"])
@login_required
def newblog():
  form = NewBlogForm()
  if form.validate_on_submit():
    blog= Blog(title=form.title.data, author=form.author.data, description=form.description.data, blog=form.blog.data)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.home'))
  return render_template('newblog.html',form=form)

@main.route('/comment/<id>',methods=['POST', 'GET'])
@login_required
def comment(id):
  form = AddComment()
  blog = Blog.query.filter_by(id = blogs.id).first()
  if form.validate_on_submit():
    comment = form.comment.data
    new_comment = Comment(comment = comment,user_id=current_user.id,blog_id=id)
    db.session.add(new_comment)
    db.session.commit()
    comments = Comment.query.filter_by(blog_id=id).all()
    return render_template("home.html",blog=blog,comments=comments,form=form)
  comments=Comment.query.filter_by(blog_id = id)
  return render_template("home.html",form=form,comments=comments)



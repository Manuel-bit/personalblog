from wtforms import  StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,ValidationError
from ..models import Blog
from flask_wtf import FlaskForm

class NewBlogForm(FlaskForm):
  title=StringField('Title',validators=[DataRequired()])
  author=StringField('Author Name',validators=[DataRequired()])
  description=TextAreaField('Short desctription',validators=[DataRequired()])
  blog=TextAreaField('My Blog',validators=[DataRequired()])
  submit=SubmitField('Save Blog')

  def validate_title(self,data_field):
    if Blog.query.filter_by(title = data_field.data).first():
      raise ValidationError('Blog with that title exists')

class AddComment(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Add Comment')
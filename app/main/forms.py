from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    description = TextAreaField("What would you like to Blog?", validators = [Required()])
    submit = SubmitField('Submit')
class CategoryForm(FlaskForm):
    name = StringField('Category', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comments', validators = [Required()])
    submit = SubmitField('Submit')

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    bio = TextAreaField('About Me')
    submit = SubmitField('Update Profile')
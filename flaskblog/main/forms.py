from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User
from wtforms.fields.html5 import DateField

class Contact(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    message = TextAreaField('Message', validators=[DataRequired()])
    
    submit = SubmitField('Send Message')
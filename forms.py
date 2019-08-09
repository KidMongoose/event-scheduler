from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, DateField, SubmitField


class LoginForm(FlaskForm):
   username_or_email = StringField('Username', [DataRequired()])
   password = PasswordField('Password', [DataRequired()])
   submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
   username = StringField('Username', [DataRequired()])
   email = StringField('E-mail', [DataRequired()])
   password = PasswordField('Password', [DataRequired()])
   submit = SubmitField('Register')


class EventForm(FlaskForm):
   event_name = StringField('Event name')
   speaker = StringField('Speaker')
   venue = StringField('Venue')
   event_date = DateField('Event date')
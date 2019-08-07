from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, DateField, SubmitField


class LoginForm(FlaskForm):
   username = StringField('Username', [DataRequired()])
   email =  StringField('E-mail', [DataRequired()])
   password = PasswordField('Password', [DataRequired()])
<<<<<<< HEAD
<<<<<<< HEAD
   submit = SubmitField('Login')
=======
>>>>>>> c4e63932d5659b6846aaea8df5e25c7689eb7e8e
=======
>>>>>>> bc830f568117864b2a684fb9f5fa58a641c15454

class EventForm(FlaskForm):
   event_name = StringField('Event name')
   speaker = StringField('Speaker')
   venue = StringField('Venue')
   event_date = DateField('Event date')
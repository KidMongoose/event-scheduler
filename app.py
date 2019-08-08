from flask import Flask, render_template
from flask_pymongo import PyMongo
from forms import *

app = Flask(__name__)
app.config['MONGO_URI'] = 'MONGO URI HERE'
app.config['SECRET_KEY'] = 'SECRET KEY HERE'
mongo = PyMongo(app)

@app.route('/')
def index():
   form = LoginForm() 
   return render_template('index.html', form = form)

@app.route('/events')
def events():
   events = mongo.db.User.find({}) 
   return render_template('events.html', events = events)

@app.route('/add/event/')
def add_event(): 
   return render_template('event.html') 

@app.route('/remove/event')
def remove_event():
   return render_template('event.html')

@app.route('/edit/event')
def edit_event():
   return render_template('event.html')

@app.route('/settings')
def settings():
   return render_template('settings.html')

if __name__ == '__main__':
   app.run()











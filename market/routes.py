from market import app
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from market.models import Pitch
from market.data import Pitches
from market.forms import RegisterForm

Pitches=Pitches()

@app.route('/')

def index():
        return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')            


@app.route('/pitch')
def pitch():
    pitches = Pitch.query.all()
    return render_template('pitch.html', pitches=Pitches)

@app.route('/pitches/<string:id>/')
def pitches(id):
    return render_template('pitches.html', id=id)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)    
    



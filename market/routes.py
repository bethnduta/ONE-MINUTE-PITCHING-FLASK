from market import app
from flask import flash, render_template, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from market.models import Pitch,User
from market.data import Pitches
from market.forms import RegisterForm
from market import db

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


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect('/')
    if form.errors != {}:
            for err_msg in form.errors.values():
                flash(f'There was an error when signing up: {err_msg}', category='danger')
    return render_template('register.html', form=form)    
    



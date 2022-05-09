from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from data import Pitches


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitch.db'
db = SQLAlchemy(app)

class Pitch(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=25), nullable=False, unique=True)
    body = db.Column(db.String(length=1000), nullable=False, unique=True)
    author = db.Column(db.String(length=30), nullable=False, unique=True)

    def __repr__(self):
        return f'Pitch{self.title}'
    



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

if __name__ == '__main__':
    app.run(debug=True)
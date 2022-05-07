from flask import Flask, render_template
from data import Pitches
app =Flask(__name__)

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
    return render_template('pitch.html', pitches=Pitches)

@app.route('/pitches/<string:id>/')
def pitches(id):
    return render_template('pitches.html', id=id)    

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from market.data import Pitches
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.models import User



app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitch.db'
app.config['SECRET_KEY'] = '08ddf6a183046d486aab6582'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import routes
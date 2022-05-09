from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username  =db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    # Pitches = db.relationship('pitch', backref='owned_user', lazy=True)


class Pitch(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=25), nullable=False, unique=True)
    body = db.Column(db.String(length=1000), nullable=False, unique=True)
    author = db.Column(db.String(length=30), nullable=False, unique=True)
    # owner = db.Column(db.integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Pitch{self.title}'
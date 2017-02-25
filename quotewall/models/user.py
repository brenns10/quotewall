# -*- coding: utf-8 -*-
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from quotewall import db
from quotewall import login_manager


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    username = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=False)
    real_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    posts = db.relationship('Quote', back_populates='poster',
                            foreign_keys='Quote.poster_id')
    quotes = db.relationship('Quote', back_populates='quoted',
                             foreign_keys='Quote.quoted_id')
    ratings = db.relationship('QuoteRating', back_populates='user',
                              foreign_keys='QuoteRating.user_id')

    def __init__(self, username, email, password, real_name):
        self.username = username
        self.email = email
        self.real_name = real_name
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # below are required for flask-login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(str_id):
    """Returns a user by the unicode id, or None."""
    try:
        int_id = int(str_id)
    except ValueError:
        return None
    return User.get(int_id)

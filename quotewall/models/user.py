# -*- coding: utf-8 -*-
from quotewall import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    username = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=False)
    real_name = db.Column(db.String, nullable=False)

    posts = db.relationship('Quote', back_populates='poster',
                            foreign_keys='Quote.poster_id')
    quotes = db.relationship('Quote', back_populates='quoted',
                             foreign_keys='Quote.quoted_id')
    ratings = db.relationship('QuoteRating', back_populates='user',
                              foreign_keys='QuoteRating.user_id')

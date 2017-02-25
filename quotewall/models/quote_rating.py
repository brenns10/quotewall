# -*- coding: utf-8 -*-
from sqlalchemy.sql import func

from quotewall import db


class QuoteRating(db.Model):
    __tablename__ = 'quote_ratings'

    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.id'),
                         primary_key=True, nullable=False)
    quote = db.relationship('Quote', back_populates='ratings')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        primary_key=True, nullable=False)
    user = db.relationship('User', back_populates='ratings')

    rating = db.Column(db.Integer, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=func.now())

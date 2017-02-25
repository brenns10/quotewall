# -*- coding: utf-8 -*-
from sqlalchemy.sql import func

from quotewall import db


class Quote(db.Model):
    __tablename__ = 'quotes'

    def __init__(self, text, quoted, poster):
        self.text = text
        self.quoted = quoted
        self.poster = poster

    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          nullable=False)
    poster = db.relationship("User", back_populates='posts',
                             foreign_keys=poster_id)
    quoted_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          nullable=False)
    quoted = db.relationship('User', back_populates='quotes',
                             foreign_keys=quoted_id)
    text = db.Column(db.Text, nullable=False)

    time_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=func.now())

    rating_count = db.Column(db.Integer, nullable=False, default=0)
    rating_sum = db.Column(db.Integer, nullable=False, default=0)

    ratings = db.relationship('QuoteRating', back_populates='quote')

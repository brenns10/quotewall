# -*- coding: utf-8 -*-
from quotewall import db
from quotewall.models.quote import Quote


def create_quote(text, quoted, poster):
    quote = Quote(text, quoted, poster)
    db.session.add(quote)
    db.session.commit()
    return quote


def get_recent_quotes(limit=10):
    return Quote.query.order_by(Quote.time_created).limit(limit).all()


def get_quote_by_id(id):
    return Quote.query.get(id)


def get_recent_quotes_by_user(user, limit=5):
    return user.quotes.limit(limit).all()

def get_recent_submissions_by_user(user, limit=5):
    return user.posts.limit(limit).all()

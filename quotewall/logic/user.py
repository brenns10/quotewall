# -*- coding: utf-8 -*-
from quotewall.models.user import User


def authenticate_user(username, password):
    user = User.query.filter(User.username == username).one()
    if not user:
        return None
    if user.check_password(password):
        return user
    else:
        return None


def get_by_username(username):
    return User.query.filter(User.username == username).one_or_none()

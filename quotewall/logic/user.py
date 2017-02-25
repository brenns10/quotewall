# -*- coding: utf-8 -*-
from quotewall.models.user import User


def authenticate_user(username, password):
    print('authenticate_user({}, {})'.format(username, password))
    try:
        user = User.query.filter(User.username == username).one()
        print(user)
    except Exception as e:
        print(e)
        return None
    print(user.password)
    if user.check_password(password):
        return user
    else:
        return None

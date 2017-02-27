# -*- coding: utf-8 -*-
import getpass

from quotewall import db
from quotewall import manager
from quotewall.models.user import User


@manager.command
def init_db():
    'creates the database schema - on first run only'
    db.create_all()


@manager.command
def add_user():
    'adds a user based on prompts'
    username = input('Username: ')
    email = input('Email: ')
    password = getpass.getpass()
    real_name = input('Real Name: ')
    user = User(username, email, password, real_name)
    db.session.add(user)
    db.session.commit()
    print('Added user!')

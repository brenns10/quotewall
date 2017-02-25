# -*- coding: utf-8 -*-
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from quotewall import app
from quotewall.logic.user import authenticate_user


@app.route('/')
def home():
    return 'hello'


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    # TODO: CSRF check
    username = request.form.get('username')
    password = request.form.get('password')
    user = authenticate_user(username, password)
    if user:
        flash('Logged in successfully!')
        next = request.args.get('next')
        return redirect(next or url_for('home'))
    else:
        flash('Username or password incorrect.')
        return render_template('login.html')

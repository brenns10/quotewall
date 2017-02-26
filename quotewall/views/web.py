# -*- coding: utf-8 -*-
from flask import abort
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user

from quotewall import app
from quotewall.logic.quote import create_quote
from quotewall.logic.quote import get_recent_quotes
from quotewall.logic.quote import get_quote_by_id
from quotewall.logic.quote import get_recent_quotes_by_user
from quotewall.logic.quote import get_recent_submissions_by_user
from quotewall.logic.user import authenticate_user
from quotewall.logic.user import get_by_username
from quotewall.models.user import User


@app.route('/')
@login_required
def home():
    recent_quotes = get_recent_quotes()
    all_users = User.query.all()
    return render_template('home.html', recent_quotes=recent_quotes,
                           all_users=all_users)


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
        login_user(user)
        flash('Logged in successfully!', 'success')
        next = request.args.get('next')
        # TODO: check for safe redirect
        return redirect(next or url_for('home'))
    else:
        flash('Username or password incorrect.', 'error')
        return render_template('login.html')


@app.route('/quote', methods=['POST'])
@login_required
def quote():
    # TODO: CSRF check
    text = request.form.get('text')
    if not text:
        flash('Enter a quote.', 'error')
        return redirect(url_for('home'))
    quoted_username = request.form.get('quoted')
    if not quoted_username:
        flash('Enter a username.', 'error')
        return redirect(url_for('home'))
    quoted = get_by_username(quoted_username)
    if not quoted:
        flash('Username {} does not exist.'.format(quoted_username), 'error')
        return redirect(url_for('home'))
    create_quote(text, quoted, current_user)
    flash('Created quote!', 'success')
    # TODO: redirect to newly created quote
    return redirect(url_for('home'))


@app.route('/quote/<int:quote_id>', methods=['GET'])
@login_required
def view_quote(quote_id):
    quote = get_quote_by_id(quote_id)
    if not quote:
        abort(404)
    return render_template('quote.html', quote=quote)


@app.route('/user/<string:username>', methods=['GET'])
@login_required
def view_user(username):
    user = get_by_username(username)
    if not user:
        abort(404)
    return render_template(
        'user.html', user=user, quotes=get_recent_quotes_by_user(user),
        submissions=get_recent_submissions_by_user(user),
    )

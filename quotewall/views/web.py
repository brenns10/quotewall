# -*- coding: utf-8 -*-
import random

from flask import abort
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
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
from quotewall.logic.registration_link import create_registration_link
from quotewall.logic.registration_link import delete_link_by_uuid
from quotewall.logic.registration_link import get_all_links
from quotewall.logic.registration_link import register_user
from quotewall.logic.user import authenticate_user
from quotewall.logic.user import get_by_username
from quotewall.models.user import User
from quotewall.util.decorators import admin_required
from quotewall.util.exc import UserException


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


@app.route('/quote', methods=['GET'])
@login_required
def quote_form():
    return render_template('new_quote.html')


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
    return render_template(
        'loading.html', target=url_for('home'), seconds=random.randint(1, 3),
        message=random.choice(app.config['LOADING_MESSAGES']),
    )


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


@app.route('/admin/links', methods=['GET'])
@admin_required
def view_links():
    links = get_all_links()
    return render_template('admin_links.html', links=links)


@app.route('/admin/links', methods=['POST'])
@admin_required
def new_link():
    count = request.form.get('uses', '1')
    try:
        uses = int(count)
    except ValueError:
        flash('Bad uses', 'error')
        return redirect(url_for('new_link'))
    link = create_registration_link(uses=uses)
    flash('Created link {}.'.format(link.uuid), 'success')
    return redirect(url_for('view_links'))


@app.route('/admin/links/delete/<string:uuid>', methods=['GET'])
@admin_required
def delete_link(uuid):
    if delete_link_by_uuid(uuid):
        flash('Deleted {}'.format(uuid), 'success')
        return redirect(url_for('view_links'))
    else:
        flash('{} does not exist.'.format(uuid), 'error')
        return redirect(url_for('view_links'))


@app.route('/register/<string:uuid>', methods=['GET'])
def register(uuid):
    if not current_user.is_anonymous:
        abort(401)
    return render_template('register.html', uuid=uuid, show_form=True)


@app.route('/register/<string:uuid>', methods=['POST'])
def register_post(uuid):
    if not current_user.is_anonymous:
        abort(401)
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    name = request.form.get('name')
    if not username or not password or not email or not name:
        flash('All fields are required.', 'error')
        return redirect(url_for('register_post', uuid=uuid))
    try:
        user = register_user(uuid, username, email, password, name)
        login_user(user)
        return redirect(url_for('home'))
    except UserException as e:
        flash(e.user_message, 'error' if e.is_error else 'success')
        return redirect(url_for('register_post', uuid=uuid))

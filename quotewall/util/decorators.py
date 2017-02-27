# -*- coding: utf-8 -*-
from functools import wraps

from flask import abort
from flask_login import current_user
from flask_login import login_required


def admin_required(func):
    """
    Use instead of login_required in order to require an admin user.
    """
    @login_required
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            abort(401)  # Unauthorized
        return func(*args, **kwargs)
    return decorated_view

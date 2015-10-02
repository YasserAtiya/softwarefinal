from flask import g, redirect, url_for, request
from functools import wraps


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect((url_for('login', next=request.url)))
        return f(*args, **kwargs)
    return decorated_function



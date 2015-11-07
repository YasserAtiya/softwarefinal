from functools import wraps
from flask import abort
from flask_login import current_user

'''
Adapted from flask.pocco.org by Alex Abott
Simple User Authorization Decorator
'''


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                return abort(403)
            return f(*args, **kwargs)

        return wrapped

    return wrapper

from functools import wraps

from flask import request


class FormValidator(object):

    def __init__(self, error_handler=None):
        self._error_handler = error_handler

    def validate_form(self, form_cls):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if request.method == 'GET':
                    form = form_cls(formdata=request.args)
                elif request.method in ('POST', 'PUT'):
                    form = form_cls()
                else:
                    return fn(*args, **kwargs)
                if not form.validate() and self._error_handler:
                    return self._error_handler(form.errors)
                return fn(form, *args, **kwargs)
            return wrapper
        return decorator

    def error_handler(self, fn):
        self._error_handler = fn
        return fn

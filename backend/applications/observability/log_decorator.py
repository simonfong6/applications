#!/usr/bin/env python3
"""
Log input and output of flask view functions.
"""
from functools import wraps

from flask import request


class log_input_output:

    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            # Log json payload if it has one.
            if hasattr(request, 'json'):
                self.logger.info({
                    'event': 'request data',
                    'data': request.json,
                })

            result = func(*args, **kwargs)

            self.logger.info({
                'event': 'response',
                'data': result,
            })
            return result
        return decorated_function

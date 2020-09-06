#!/usr/bin/env python3
"""
Logging
"""
import logging
import json
from logging import getLogger

from applications.database.json import CustomJSONEncoder

LOGGING_LEVEL = logging.INFO
LOGGING_METHODS = [
    'debug',
    'info',
    'warning',
    'error',
    'critical',
]


def get_logger(name):
    return Logger(name)


class Logger:

    def __init__(self, name):
        self.logger = getLogger(name)
        self.logger.setLevel(LOGGING_LEVEL)

        for method in LOGGING_METHODS:
            custom = self.generate_logger_method(method)
            setattr(self, method, custom)

    def dumps(self, obj):
        return json.dumps(obj, indent=4, sort_keys=True, cls=CustomJSONEncoder)

    def generate_logger_method(self, method):
        regular = getattr(self.logger, method)
        def custom(obj):
            if isinstance(obj, dict):
                obj = self.dumps(obj)
            return regular(obj)

        return custom

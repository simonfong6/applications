#!/usr/bin/env python3
"""
Logging
"""
import logging
from logging import getLogger

LOGGING_LEVEL = logging.INFO


def get_logger(name):
    logger = getLogger(name)
    logger.setLevel(LOGGING_LEVEL)
    return logger


class Class:

    def __init__(self):
        super().__init__()


def main(args):

    pass


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-a', '--arg1',
                        help="An argument.",
                        type=str,
                        default='default')

    args = parser.parse_args()
    main(args)

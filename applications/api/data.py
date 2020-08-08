#!/usr/bin/env python3
"""
Blueprint
"""
from flask import Blueprint
from flask import jsonify


data = Blueprint('data', __name__)


@data.route('/')
def index():
    return jsonify({'data': 100})


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

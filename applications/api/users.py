#!/usr/bin/env python3
"""
Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import session

from applications.models import User


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


users = Blueprint('users', __name__)


@users.route('/')
def index():
    users = User.all()

    users = [user.json_public() for user in users]

    return jsonify(users)


@users.route('/new', methods=['POST'])
def create():
    data = request.json

    user = User.build_from_json(data)

    if user.exists():
        return jsonify({
            'error': 'User with that email already exists.',
            'msg': 'User already exists, please login in.'
        })

    user.save()

    return jsonify(user.json_public())


@users.route('/current')
def current():
    logger.info(f"Session: {session}")

    if 'email' not in session:
        return jsonify(
            status='No user'
        )

    email = session['email']

    user = User.find(email)

    return jsonify(user.json_public())


@users.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.build_from_json(data)

    logger.info(f"Logging in email: '{user.email}'")

    if not user.exists():
        logger.info(f"User '{user.email}' does not exist.")
        return jsonify({
            'status': 'Failed',
            'msg': 'Email not found, please signup.'
        })

    password = data['password']
    user = User.find(user.email)

    if not user.match(password):
        logger.info('Login failed.')
        return jsonify({
            'status': 'Failed',
            'msg': 'Incorrect password.'
        })

    logger.info('Login successful.')

    session['email'] = user.email

    logger.info(f'Added email to session {session["email"]}')
    return jsonify({
        'status': 'success',
        'msg': 'Login successful.'
    })


@users.route('/logout')
def logout():
    if 'email' not in session:
        return jsonify({
            'status': 'Not Logged in.',
            'msg': 'Cannto log out.'
        })

    # Remove the email from the session if it's there
    session.pop('email', None)

    return jsonify({
        'status': 'Logged Out'
    })


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

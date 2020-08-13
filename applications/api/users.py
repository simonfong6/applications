#!/usr/bin/env python3
"""
Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from applications.authentication import generate
from applications.authentication import match
from applications.database.table import Table
from applications.models.user import User


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


users = Blueprint('users', __name__)


table = Table('users')


@users.route('/')
def index():
    users = []

    users = table.get_all()

    return jsonify(users)


@users.route('/new', methods=['POST'])
def create():

    data = request.json

    email = data['email']
    password = data['password']

    user = table.get({
        'email': email
    })

    logger.info(f'User: {user}')

    if user:
        return jsonify({
            'error': 'User with that email already exists.',
            'msg': 'User already exists, please login in.'
        })


    salt, hashcode = generate(password)
    
    uuid = User.create_uuid()

    user = {
        'uuid': uuid,
        'salt': salt,
        'email': email,
        'hash': hashcode

    }

    logger.info(f"Creating user :'{user}'")

    table.put(user)

    return jsonify(user)


@users.route('/current')
def current():

    logger.info(f"Session: {session}")
    email_key = 'email'

    if email_key not in session:
        return jsonify(
            status='No user'
        )

    email = session[email_key]

    user = table.get({
        'email': email
    })

    # Remove sensitive data.
    del user['salt']
    del user['hash']

    return jsonify(user)


@users.route('/login', methods=['POST'])
def login():

    if request.json:
        data = request.json
        logger.info(data)

    email = data['email']
    password = data['password']
    logger.info(f"Logging in email: '{email}'")

    user = table.get({
        'email': email
    })

    if not user:
        logger.info(f"User '{email}' does not exist.")
        return jsonify({
            'status': 'Failed',
            'msg': 'Email not found, please signup.'
        })
    
    salt = user['salt']
    hashcode = user['hash']

    if not match(password, salt, hashcode):
        logger.info('Login failed.')
        return jsonify({
            'status': 'Failed',
            'msg': 'Incorrect password.'
        })

    logger.info('Login successful.')

    session['email'] = email

    logger.info(f'Added email to session {session["email"]}')
    return jsonify({
        'status': 'success',
        'msg': 'Login successful.'
    })


@users.route('/logout')
def logout():
    # remove the username from the session if it's there
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

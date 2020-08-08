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
from applications.table import Table
from applications.user import User


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


users = Blueprint('users', __name__)


@users.route('/')
def index():
    users = []

    table = Table('users')

    users = table.get_all()

    return jsonify(users)


@users.route('/new', methods=['POST'])
def create():

    data = request.json

    email = data['email']
    password = data['password']

    salt, hashcode = generate(password)
    
    uuid = User.create_uuid()

    user = {
        'uuid': uuid,
        'salt': salt,
        'email': email,
        'hash': hashcode

    }

    logger.info(f"Creating user :'{user}'")

    table = Table('users')

    table.put(user)

    return jsonify(user)


# @users.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'

@users.route('/current')
def current():

    email_key = 'email'

    if email_key not in session:
        return jsonify(
            status='No user'
        )

    email = session[email_key]

    table = Table('users')

    user = table.get({
        'email': email
    })

    return jsonify(user)


@users.route('/login', methods=['POST'])
def login():

    if request.json:
        data = request.json
        print(data)

    email = 'key@gmail.com'
    logger.info(f"Logging in email: '{email}'")

    session['email'] = email
    return redirect(url_for('users.current'))


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

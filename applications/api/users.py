#!/usr/bin/env python3
"""
Blueprint
"""
import logging

from bcrypt import gensalt
from bcrypt import hashpw
from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import request
from flask import session
from flask import url_for

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

    salt = gensalt()

    password = password.encode('utf-8')

    password_hash = hashpw(password, salt).decode('utf-8')
    
    uuid = User.create_uuid()

    user = {
        'uuid': uuid,
        'salt': salt.decode('utf-8'),
        'email': email,
        'hash': password_hash

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


@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@users.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


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

#!/usr/bin/env python3
"""
Backend server.
"""
import logging
import os

from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from markupsafe import escape

from applications.dynamo_db import DynamoDB
from applications.table import Table

# Configure logging.
logging.basicConfig(filename='logs/server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.getenv('FLASK_SECRET_KEY')


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/api/data')
def data():
    return jsonify({'data': 100})

@app.route('/api/company/new', methods=['POST'])
def company():

    data = request.json

    table = Table('companies')

    name = data['company']
    
    logger.info(f"Creating company: '{name}'")
    table.put({
        'name': name
    })

    company = table.get({
        'name': name
    })

    return jsonify(company)


@app.route('/api/companies')
def get_companies():
    companies = []

    table = Table('companies')

    request = table.table.scan()

    companies = request['Items']

    return jsonify(companies)


def main(args):

    if args.debug:
        logger.setLevel(logging.DEBUG)

    app.run(
        host='0.0.0.0',
        debug=args.debug,
        port=args.port
    )


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-p', '--port',
                        help="Port that the server will run on.",
                        type=int,
                        default=8000)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False,
                        action='store_true')

    args = parser.parse_args()
    main(args)

#!/usr/bin/env python3
"""
Backend server.
"""
import logging

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from applications.dynamo_db import DynamoDB
from applications.table import Table

# Configure logging.
logging.basicConfig(filename='logs/server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html.jinja')

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

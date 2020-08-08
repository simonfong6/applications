#!/usr/bin/env python3
"""
Backend server.
"""
import logging
import os

from flask import Flask
from flask_cors import CORS

from applications.api import register_sub_site


# Configure logging.
logging.basicConfig(filename='logs/server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)


def setup(app):

    # Cors to allow proxy from React app.
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register routes.
    register_sub_site(app)

    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = os.getenv('FLASK_SECRET_KEY')


def main(args):

    setup(app)

    if args.debug:
        logger.setLevel(logging.DEBUG)

    logger.info(app.url_map)

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

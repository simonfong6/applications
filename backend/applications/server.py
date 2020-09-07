#!/usr/bin/env python3
"""
Backend server.
"""
import logging
import os
import sys

from flask import Flask
from flask_cors import CORS

from applications.api import register_sub_site
from applications.database import initialize as initialize_database
from applications.database.json import CustomJSONEncoder
from applications.observability import get_logger


# Configure logging.
logging.basicConfig(stream=sys.stdout)
logger = get_logger(__name__)


app = Flask(
    __name__,
    static_folder='/code/build',  # Serve the React files.
    static_url_path='/'
)



FRONTEND_PROXY = 'http://localhost:3000'


def setup(app):

    # Cors to allow proxy from React app.
    CORS(
        app,
        resources={r"/api/*": {"origins": FRONTEND_PROXY}},
        supports_credentials=True
    )

    # Register routes.
    logger.info({'action': 'Registering routes.'})
    register_sub_site(app)

    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = os.getenv('FLASK_SECRET_KEY')

    # Allow encoding of BSON objects for MongoDB.
    app.json_encoder = CustomJSONEncoder

    # Initialize database.
    initialize_database()


# Allow fetching root serves index file.
@app.route('/')
def index():
    logger.info("Hitting index.")
    return app.send_static_file('index.html')

@app.route('/time')
def time():
    from time import time
    logger.info("Hitting time.")
    return {
        "time": time(),
        "version": 0.1
    }

setup(app)

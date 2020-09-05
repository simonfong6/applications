#!/usr/bin/env python3
"""
MongoDB Client
"""
from os import environ
from urllib.parse import quote_plus

from flask import g
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from applications.observability import get_logger


logger = get_logger(__name__)

DATABASE_NAME_KEY = 'MONGO_DATABASE'
DATABASE_HOST_KEY = 'MONGO_HOST'
DATABASE_USERNAME_KEY = 'MONGO_USERNAME'
DATABSE_PASSWORD_KEY = 'MONGO_PASSWORD'
DATBASE_CONNECTION_TIMEOUT_MS = 3000


def get_from_env_with_error(key):
    value = environ.get(key, None)
    if value is None:
        msg = f"{key} not in environment variable."
        logger.warning(msg)
    return value


def get_client():
    host = get_from_env_with_error(DATABASE_HOST_KEY)
    user = get_from_env_with_error(DATABASE_USERNAME_KEY)
    password = get_from_env_with_error(DATABSE_PASSWORD_KEY)

    if not all([host, user, password]):
        return

    user = quote_plus(user)
    password = quote_plus(password)

    uri = f'mongodb://{user}:{password}@{host}'
    
    try:
        client = MongoClient(
            uri,
            serverSelectionTimeoutMS=DATBASE_CONNECTION_TIMEOUT_MS
        )
        client.server_info()
    except ServerSelectionTimeoutError as error:
        logger.error(f"Mongo connection failed in {DATBASE_CONNECTION_TIMEOUT_MS} milliseconds")
        print(error)
        return None

    return client


def get_database():
    name = get_from_env_with_error(DATABASE_NAME_KEY)

    if name is None:
        return

    name = environ.get(DATABASE_NAME_KEY, None)

    client = get_client()
    if not client:
        logger.warning(f"No database.")
        return None

    database = client[name]

    return database

def get_flask_database():
    if 'database' not in g:
        g.database = get_database()

    return g.database

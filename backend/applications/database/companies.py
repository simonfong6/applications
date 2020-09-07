#!/usr/bin/env python3
"""
Companies Collection Initialization
"""
from pymongo import ASCENDING

from applications.database.client import get_database
from applications.observability import get_logger


logger = get_logger(__name__)


COLLECTION_NAME = 'companies'


def initialize():
    logger.info(
        {
            'action': 'Creating indices.',
            'collection': COLLECTION_NAME
        }
    )
    database = get_database()
    collection = database[COLLECTION_NAME]

    collection.create_index(
        [
            ('name', ASCENDING)
        ],
        unique=True
    )


if __name__ == '__main__':
    intialize()

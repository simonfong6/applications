#!/usr/bin/env python3
"""
Blueprint
"""
from flask import Blueprint
from flask import jsonify

from applications.database import get_flask_database
from applications.observability import get_logger


logger = get_logger(__name__)


data = Blueprint('data', __name__)


@data.route('/')
def index():
    return jsonify({'data': 100})

@data.route('/mongo')
def mongodb():
    database = get_flask_database()

    posts = database.posts

    import datetime

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }

    post_id = posts.insert_one(post).inserted_id

    posts = database.posts

    cursor = posts.find({})
    docs = []
    for document in cursor:
        docs.append(document)
        logger.info(document)
    return jsonify(docs)


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

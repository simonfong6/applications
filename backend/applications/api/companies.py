#!/usr/bin/env python3
"""
Companies Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request
from pymongo.errors import DuplicateKeyError

from applications.models import Company
from applications.database import get_flask_database
from applications.links.site_checker import get_careers_page
from applications.observability import get_logger


logger = get_logger(__name__)


companies = Blueprint('companies', __name__)

def get_collection():
    database = get_flask_database()
    return database.companies


@companies.route('/')
def index():
    companies = get_collection()
    cursor = companies.find({
        'deleted': {"$ne": True}
    })
    documents = [document for document in cursor]

    return jsonify(documents)


@companies.route('/new', methods=['POST'])
def create():
    data = request.json
    logger.info({
        'action': 'Creating',
        'data': data,
    })

    name = data['company']
    manual_link = data.get('link', None)

    document = {
        'name': name,
        'auto_link': get_careers_page(name),
        'career_link': manual_link,
        'links': {
            'auto': get_careers_page(name),
            'manual': manual_link,
        },
        'deleted': False,
    }

    logger.info({
        'action': 'Inserting',
        'document': document,
    })

    companies = get_collection()

    try:
        id_ = companies.insert_one(document).inserted_id

        logger.info({
            'event': 'Inserted',
            'id': id_,
        })

        document = companies.find_one({"_id": id_})
        response = {
            'status': 'Created',
            'document': document,
        }
    except DuplicateKeyError as error:
        logger.info({
            'event': 'Duplicate key',
            'error': str(error),
        })

        # If deleted, undelete.
        logger.info({
            'event': 'recreate',
            'message': 'Setting delete to false.',
        })
        companies.update_one(
            {
                'name': name,
            },
            {
                '$set': {
                    'deleted': False,
                },
            },
        )

        response = {
            'status': 'error',
            'error': 'Company name already exists.',
        }

    return response


@companies.route('/<name>', methods=['DELETE'])
def delete(name):
    logger.info({
        'event': 'Delete',
        'resource': name,
    })
    companies = get_collection()

    companies.update_one(
        {
            'name': name,
        },
        {
            '$set': {
                'deleted': True,
            },
        },
    )

    response = {
        'status': 'deleted',
        'name': name,
    }

    return response

#!/usr/bin/env python3
"""
Jobs Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request

from applications.database import get_flask_database
from applications.database.unique_id import create_uuid
from applications.database.table import Table
from applications.models import Company
from applications.models import Job
from applications.observability import get_logger
from applications.observability import log_input_output


logger = get_logger(__name__)


jobs = Blueprint('jobs', __name__)


COLLECTION_NAME = 'jobs'

def has_json(request):
    return hasattr(request, 'json')


def get_collection():
    database = get_flask_database()
    return database[COLLECTION_NAME]


@jobs.route('/')
def index():
    jobs = get_collection()
    cursor = jobs.find({
        'deleted': {"$ne": True}
    })
    documents = [document for document in cursor]

    return jsonify(documents)


@jobs.route('/new', methods=['POST'])
@log_input_output(logger)
def create():
    if not has_json(request):
        return {
            'error': 'no json payload'
        }

    data = request.json

    # Check if company is in database.
    database = get_flask_database()
    companies = database.companies
    name = data['company']
    company = companies.find_one({'name': name})

    if company is None:
        return {
            'error': 'no company found',
            'company': name,
        }

    data['company'] = company

    jobs = get_collection()

    inserted_id = jobs.insert_one(data).inserted_id

    data['_id'] = inserted_id

    return {
        'event': 'created job',
        'job': data,
    }

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


logger = get_logger(__name__)


jobs = Blueprint('jobs', __name__)


COLLECTION_NAME = 'jobs'

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

    jobs = Job.all()

    jsonified = []
    for job in jobs:
        company = job.get_company()
        company_json = company.json()
        company_json['url'] = company.auto_link

        job_json = job.json()
        job_json['company'] = company_json

        jsonified.append(job_json)

    return jsonify(jsonified)


@jobs.route('/new', methods=['POST'])
def create():
    data = request.json

    job = Job.build(data)

    job.save()

    return jsonify(job.json())


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

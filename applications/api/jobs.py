#!/usr/bin/env python3
"""
Jobs Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request

from applications.database.unique_id import create_uuid
from applications.table import Table


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


jobs = Blueprint('jobs', __name__)


table = Table('jobs')


@jobs.route('/')
def index():
    jobs = []

    jobs = table.get_all()

    return jsonify(jobs)


@jobs.route('/new', methods=['POST'])
def create():

    data = request.json

    uuid = create_uuid()
    company = data['company']
    url = data['url']
    role = data['role']
    type_ = data['type']
    
    logger.info(f"Creating Job: '{url}'")
    table.put({
        'uuid': uuid,
        'company': company,
        'url': url,
        'role': role,
        'type': type_,
    })

    job = table.get({
        'uuid': uuid
    })

    return jsonify(job)


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

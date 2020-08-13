#!/usr/bin/env python3
"""
Companies Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request

from applications.models import Company
from applications.observability import get_logger


logger = get_logger(__name__)


companies = Blueprint('companies', __name__)


@companies.route('/')
def index():
    companies = Company.all()

    return jsonify(companies)


@companies.route('/new', methods=['POST'])
def create():
    data = request.json
    logger.info(data)

    item = {}
    item['name'] = data['company']

    company = Company.build(item)

    company.save()

    return company.json()


@companies.route('/<name>', methods=['DELETE'])
def delete(name):
    Company.delete(name)

    return {'status': 'deleted'}


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

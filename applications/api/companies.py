#!/usr/bin/env python3
"""
Companies Blueprint
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request

from applications.links.site_checker import get_careers_page
from applications.database.table import Table


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


companies = Blueprint('companies', __name__)


@companies.route('/')
def index():
    companies = []

    table = Table('companies')

    companies = table.get_all()

    return jsonify(companies)


@companies.route('/new', methods=['POST'])
def create():

    data = request.json

    table = Table('companies')

    name = data['company']

    auto_link = get_careers_page(name)
    
    logger.info(f"Creating company: '{name}'")
    table.put({
        'name': name,
        'auto_link': auto_link
    })

    company = table.get({
        'name': name
    })

    return jsonify(company)


@companies.route('/<company>', methods=['DELETE'])
def delete(company):
    table = Table('companies')

    table.delete({
        'name': company
    })

    return jsonify({'status': 'deleted'})


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

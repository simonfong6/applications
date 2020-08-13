#!/usr/bin/env python3
"""
Class
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import session

from applications.database.table import Table
from applications.models import UserJob


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


users_jobs = Blueprint('users/jobs', __name__)


table = Table('users_jobs')
users_table = Table('users')


@users_jobs.route('/')
def index():

    if 'email' not in session:
        return jsonify({
            'status': 'Not Signed In',
            'msg': 'Please sign in.'
        })

    email = session['email']

    user = users_table.get({
        'email': email
    })

    user_uuid = user['uuid']

    user_jobs = UserJob.all_for_user(user_uuid)

    return jsonify(user_jobs)


@users_jobs.route('/new', methods=['POST'])
def create():
    if 'email' not in session:
        return jsonify({
            'status': 'Not Signed In',
            'msg': 'Please sign in.'
        })

    email = session['email']

    user = users_table.get({
        'email': email
    })


    data = request.json

    job_uuid = data['uuid']

    logger.info(data)

    user_job = UserJob()

    user_job.user_uuid = user['uuid']
    user_job.job_uuid = job_uuid

    user_job.save()

    return jsonify(user_job.json())


@users_jobs.route('/update', methods=['POST'])
def update():
    if 'email' not in session:
        return jsonify({
            'status': 'Not Signed In',
            'msg': 'Please sign in.'
        })

    email = session['email']

    user = users_table.get({
        'email': email
    })


    data = request.json

    user_job_uuid = data['uuid']

    user_job = UserJob.get({
        'user_uuid': user['uuid'],
        'uuid': user_job_uuid
    })

    status = data['status']

    if status == 'Applied':
        user_job.timestamp_applied = UserJob.create_timestamp()

    user_job.status = status

    user_job.save()

    return jsonify(user_job.json())


class Class:

    def __init__(self):
        super().__init__()


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

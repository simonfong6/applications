#!/usr/bin/env python3
"""
UserJob
"""
import logging
from decimal import Decimal

from boto3.dynamodb.conditions import Key

from applications.table import Table
from applications.database.timestamp import micros


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


table = Table('users_jobs')
jobs_table = Table('jobs')
companies_table = Table('companies')


class UserJob:

    TABLE_NAME = 'users_jobs'

    def __init__(self):
        super().__init__()
        self.timestamp = None
        self.user_uuid = None
        self.job_uuid = None
        self.status = None
        self.timestamp_applied = None
        self.timestamp_rejected = None
        self.timestamp_email = None
        self.timestamp_coding_challenge = None
        self.timestamp_interview = None
        self.timestamp_onsite = None
        self.timestamp_offer = None
        self.timestamp_offer_accepted = None
        self.timestamp_offer_rejected = None

    def json(self):
        data = {
            'user_uuid': self.user_uuid,
            'timestamp': self.timestamp,
            'job_uuid': self.job_uuid,
            'status': self.status,
            'timestamp_applied': self.timestamp_applied,
            'timestamp_rejected': self.timestamp_rejected,
            'timestamp_email': self.timestamp_email,
            'timestamp_coding_challenge': self.timestamp_coding_challenge,
            'timestamp_interview': self.timestamp_interview,
            'timestamp_onsite': self.timestamp_onsite,
            'timestamp_offer': self.timestamp_offer,
            'timestamp_offer_accepted': self.timestamp_offer_accepted,
            'timestamp_offer_rejected': self.timestamp_offer_rejected,
        }

        return data

    def save(self):
        if not self.user_uuid:
            logger.warn('UserJob not saved, no user uuid.')
            return

        if not self.job_uuid:
            logger.warn('UserJob not saved, no job uuid.')
            return

        if not self.status:
            logger.info('UserJob has no status, setting to not applied.')
            self.status = 'Not Applied'


        if not self.timestamp:
            self.timestamp = micros()

        data = self.json()

        table.put(data)

    @staticmethod
    def build(data):

        user_job = UserJob()

        for key, value in data:
            setattr(user_job, key, value)

        return user_job

    @staticmethod
    def get(key):
        return table.get(key)

    @staticmethod
    def all():
        items = table.get_all()

        user_jobs = []
        for item in items:
            user_job = UserJob.build(item)
            user_jobs.append(user_job)


        return user_jobs

    @staticmethod
    def all_for_user(user_uuid):

        response = table.table.query(
            KeyConditionExpression=Key('user_uuid').eq(user_uuid)
        )
        user_jobs = response['Items']

        for user_job in user_jobs:

            # Convert decimals to ints.
            for key, value in user_job.items():
                if isinstance(value, Decimal):
                    user_job[key] = int(value)

            job = jobs_table.get({
                'uuid': user_job['job_uuid']
            })

            company_name = job['company']

            company = companies_table.get({
                'name': company_name
            })

            url = company.get('auto_link', '')
            
            job['company'] = {
                'name': company_name,
                'url': url,
            }

            user_job['job'] = job

            logger.info(user_job)

        return user_jobs


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

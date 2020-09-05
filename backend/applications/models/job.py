#!/usr/bin/env python3
"""
Job Model
"""
from applications.database.table import Table
from applications.database.unique_id import create_uuid
from applications.models import Company
from applications.models.abstract import Allable
from applications.models.abstract import Deleteable
from applications.models.abstract import Existable
from applications.models.abstract import Jsonable
from applications.observability import get_logger


logger = get_logger(__name__)


class Job(
    Allable,
    Deleteable,
    Existable
):
    logger = logger

    table_name = 'jobs'
    table = Table(table_name)

    fields = [
        'uuid',
        'company',
        'url',
        'role',
        'type'
    ]

    def __init__(self):
        super().__init__()

    def get_company(self):
        return Company.find(self.company)

    def save(self):
        if not self.uuid:
            self.uuid = create_uuid()

        item = self.json()

        self.table.put(item)


def main(args):
    items = Job.all()
    # items = [item.json() for item in items]
    print(items[0])



if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-a', '--arg1',
                        help="An argument.",
                        type=str,
                        default='default')

    args = parser.parse_args()
    main(args)

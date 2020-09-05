#!/usr/bin/env python3
"""
Base
"""
from logging import Logger
from typing import List

from applications.database.table import Table


class Base:

    logger: Logger
    table: Table
    primary_key: str
    fields: List[str]

    def __init__(self):
        # Initialize all fields to None.
        for field in self.fields:
            setattr(self, field, None)


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

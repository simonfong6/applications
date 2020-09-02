#!/usr/bin/env python3
"""
Deleteable
"""
from applications.database.table import Table

from .base import Base


class Deleteable(Base):

    @classmethod
    def delete(cls, key):
        cls.logger.info(f"Deleting '{key}'")
        return cls.table.delete({
            cls.primary_key: key
        })


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

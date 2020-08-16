#!/usr/bin/env python3
"""
Findable
"""
from .base import Base
from .buildable import Buildable


class Findable(Buildable):

    @classmethod
    def find(cls, key):
        item = cls.table.get({
            cls.primary_key: key
        })

        obj = cls.build(item)
        return obj


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

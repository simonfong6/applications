#!/usr/bin/env python3
"""
Allable
"""
from applications.database.table import Table

from .base import Base
from .buildable import Buildable
from .jsonable import Jsonable


class Allable(
    Buildable,
    Jsonable
):

    @classmethod
    def all(cls, json=False):
        items = cls.table.get_all()

        objs = [cls.build(item) for item in items]

        if json:
            objs = [obj.json() for obj in objs]

        return objs


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

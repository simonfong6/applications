#!/usr/bin/env python3
"""
Jsonable
"""
from json import dumps

from .base import Base


class Jsonable(Base):

    def __repr__(self):
        dict_ = self.json()
        string = dumps(dict_, indent=4, sort_keys=True)
        repr_string = f"Job({string})"
        return repr_string

    def json(self):
        item = {}

        for field in self.fields:
            item[field] = getattr(self, field)

        return item


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

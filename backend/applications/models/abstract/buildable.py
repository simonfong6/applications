#!/usr/bin/env python3
"""
Buildable
"""
from .base import Base

class Buildable(Base):

    @classmethod
    def build(cls, item: dict):
        if item is None:
            return None

        obj = cls.__new__(cls)

        for field in cls.fields:
            value = item.get(field, None)
            setattr(obj, field, value)

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

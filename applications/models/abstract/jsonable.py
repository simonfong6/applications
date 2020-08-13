#!/usr/bin/env python3
"""
Jsonable
"""


class Jsonable:

    fields = []

    def __init__(self):
        super().__init__()

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

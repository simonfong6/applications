#!/usr/bin/env python3
"""
Base
"""
from .findable import Findable


class Existable(
    Findable
):

    def exists(self):
        key = getattr(self, self.primary_key)
        item = self.find(key)

        return item is not None


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

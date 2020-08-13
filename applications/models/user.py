#!/usr/bin/env python3
"""
User
"""
import uuid

class User:

    def __init__(self):
        super().__init__()

    @staticmethod
    def create_uuid():
        return uuid.uuid4().hex


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

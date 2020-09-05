#!/usr/bin/env python3
"""
Class
"""
from time import time


MICROSECONDS_PER_SECOND = 1000000


def micros():
    seconds = time()

    microseconds = seconds * MICROSECONDS_PER_SECOND

    microseconds = int(round(microseconds))


    return microseconds


class Class:

    def __init__(self):
        super().__init__()


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

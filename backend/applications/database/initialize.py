#!/usr/bin/env python3
"""
Initialize collections.
"""
from .companies import initialize as init_companies


def initialize():
    init_companies()


if __name__ == '__main__':
    initialize()

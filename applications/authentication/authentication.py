#!/usr/bin/env python3
"""
Authentication
"""
from bcrypt import gensalt
from bcrypt import hashpw

ENCODING = 'utf-8'


def to_string(bytes_):
    return bytes_.decode(ENCODING)


def to_bytes(string):
    return string.encode(ENCODING)


def generate(password: str):
    
    password = to_bytes(password)

    salt = gensalt()

    hashcode = hashpw(password, salt)

    salt = to_string(salt)
    hashcode = to_string(hashcode)

    return salt, hashcode


def match(password: str, salt: str, hashcode: str):
    password = to_bytes(password)
    salt = to_bytes(salt)
    hashcode = to_bytes(hashcode)

    hashcode_to_compare = hashpw(password, salt)

    return hashcode == hashcode_to_compare


def main(args):
    password = '123456'

    salt, hashcode = generate(password)

    matches = match(password, salt, hashcode)

    print(matches)

    password = '123456'

    salt, hashcode = generate(password)

    password = '1234567'

    matches = match(password, salt, hashcode)

    print(matches)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-a', '--arg1',
                        help="An argument.",
                        type=str,
                        default='default')

    args = parser.parse_args()
    main(args)

#!/usr/bin/env python3
"""
User Model
"""
from applications.authentication import generate
from applications.authentication import match
from applications.database.table import Table
from applications.database.unique_id import create_uuid
from applications.models.abstract import Jsonable
from applications.observability import get_logger


logger = get_logger(__name__)


class User(Jsonable):

    table = Table('users')
    primary_key = 'email'
    
    fields = [
        'email',
        'uuid',
        'salt',
        'hash',
    ]

    private_fields = set([
        'salt',
        'hash'
    ])

    def __init__(self):
        super().__init__()
        self.email = None
        self.uuid = None
        self.salt = None
        self.hash = None

    def json_public(self):
        item = self.json()

        item = self.sanitize(item)

        return item

    def save(self):
        if not self.email:
            raise ValueError('Email is not set.')

        if not self.salt:
            raise ValueError('Salt is not set.')

        if not self.hash:
            raise ValueError('Hash is not set.')

        if not self.uuid:
            self.uuid = create_uuid()

        if self.exists():
            raise ValueError('Email already exists.')
        
        item = self.json()

        logger.info(f"Creating user: '{self.email}'")
        self.table.put(item)

    def match(self, password):
        return match(password, self.salt, self.hash)

    @classmethod
    def build(cls, item: dict):
        if item is None:
            return None

        obj = User()

        for field in cls.fields:
            value = item.get(field, None)
            setattr(obj, field, value)

        return obj

    @classmethod
    def build_from_json(cls, item: dict):
        obj = User()

        email = item['email']
        password = item['password']

        salt, hashcode = generate(password)

        obj.email = email
        obj.salt = salt
        obj.hash = hashcode

        return obj

    @classmethod
    def find(cls, key):
        item = cls.table.get({
            cls.primary_key: key
        })

        obj = cls.build(item)
        return obj

    def exists(self):
        item = self.find(self.email)

        return item is not None

    @classmethod
    def delete(cls, key):
        logger.info(f"Deleting '{key}'")
        return cls.table.delete({
            cls.primary_key: key
        })

    @classmethod
    def sanitize(cls, item):
         # Do not expose fields like salt and password hash.
        for field in cls.private_fields:
            if field in item:
                del item[field]
        
        return item

    @classmethod
    def all(cls):
        items = cls.table.get_all()

        objs = [cls.build(item) for item in items]

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

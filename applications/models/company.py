#!/usr/bin/env python3
"""
Company Model
"""
from applications.database.table import Table
from applications.links.site_checker import get_careers_page
from applications.models.abstract import Jsonable
from applications.observability import get_logger


logger = get_logger(__name__)


class Company(Jsonable):

    table = Table('companies')
    primary_key = 'name'
    
    fields = [
        'name',
        'auto_link',
        'careers_link',
    ]

    def __init__(self):
        super().__init__()
        self.name = None
        self.auto_link = None
        self.careers_link = None
    
    def save(self):
        if not self.name:
            raise ValueError('Name is not set.')

        if not self.auto_link:
            self.auto_link = get_careers_page(self.name)
        
        item = self.json()

        logger.info(f"Creating company: '{self.name}'")
        self.table.put(item)

    @classmethod
    def build(cls, item: dict):
        obj = Company()

        for field in cls.fields:
            value = item.get(field, None)
            setattr(obj, field, value)

        return obj

    @classmethod
    def find(cls, key):
        item = cls.table.get({
            cls.primary_key: key
        })
        obj = cls.build(item)
        return obj

    @classmethod
    def delete(cls, key):
        logger.info(f"Deleting '{key}'")
        return cls.table.delete({
            cls.primary_key: key
        })

    @classmethod
    def all(cls):
        items = cls.table.get_all()

        return items


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

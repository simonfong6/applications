#!/usr/bin/env python3
"""
Database Seeding

Thanks to this blog:
https://phauer.com/2018/local-development-docker-compose-seeding-stubs/
"""
import random

from bson.objectid import ObjectId
from faker import Faker
from faker.providers import BaseProvider

from applications.database.client import get_database
from applications.observability import get_logger


logger = get_logger(__name__)

FAKER_SEED = 0
NUM_COMPANIES = 20
POSSIBLE_TAGS = ['vacation', 'business', 'technology', 'mobility', 'apparel']
fake = Faker('en')


class CustomProvider(BaseProvider):
    def url(self):
        domain = fake.domain_name()
        return f"https://{domain}"


fake.add_provider(CustomProvider)


class MongoSeeder:

    def __init__(self):
        Faker.seed(FAKER_SEED)
        self.database = get_database()

    def seed_collection(self, name, documents):
        logger.info({
            'action': 'seeding',
            'collection': name,
        })
        collection = self.database[name]     

        # Clear collection.   
        collection.remove({})

        collection.insert_many(documents)
        logger.info({
            'event': 'seeded',
            'collection': name,
        })

    def companies(self):
        documents = generate_documents(generate_company, NUM_COMPANIES)
        self.seed_collection('companies', documents)

    def seed(self):
        self.companies()


def generate_documents(generator, count):
    return [generator() for _ in range(count)]


def generate_company():
    auto_link = fake.url()
    career_link = fake.url()
    data = {
        "name": fake.company(),
        "auto_link": auto_link,
        "career_link": career_link,
        "deleted": fake.boolean(chance_of_getting_true=10),
        "links": {
            "auto": auto_link,
            "manual": career_link,
        },
        "createdTime":  fake.date_time(),
    }

    return data

def seed():
    MongoSeeder().seed()


if __name__ == '__main__':
    seed()

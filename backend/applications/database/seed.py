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
NUM_JOBS = 30


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

    def jobs(self):
        documents = generate_jobs()
        self.seed_collection('jobs', documents)

    def seed(self):
        self.companies()
        self.jobs()


def generate_documents(generator, count):
    return [generator() for _ in range(count)]


def generate_company():
    auto_link = fake.url()
    career_link = fake.url()
    data = {
        'name': fake.company(),
        'auto_link': auto_link,
        'career_link': career_link,
        'deleted': fake.boolean(chance_of_getting_true=10),
        'links': {
            'auto': auto_link,
            'manual': career_link,
        },
        'createdTime':  fake.date_time(),
    }

    return data


def generate_job(companies):
    ROLES = [
        'Software Engineer',
        'Product Manager',
        'Quantative Researcher',
        'Research Scientist',
    ]
    TYPES = [
        'Fulltime',
        'Intern',
        'Contractor',
    ]
    TAGS = [
        'New Grad',
        'University',
        'Entry Level',
        'Infrastructure',
        'Frontend',
        'Backend',
        'Fullstack',
        'Senior',
    ]

    tags = fake.random_choices(TAGS)
    tags = set(tags)
    tags = list(tags)
    data = {
        'company': fake.random_element(companies),
        'url': fake.url(),
        'role': fake.random_element(ROLES),
        'type': fake.random_element(TYPES),
        'tags': tags,
    }

    return data


def generate_jobs():
    database = get_database()
    collection = database['companies']
    cursor = collection.find({})
    companies = [doc for doc in cursor]

    return [generate_job(companies) for _ in range(NUM_JOBS)]


def seed():
    MongoSeeder().seed()


if __name__ == '__main__':
    seed()

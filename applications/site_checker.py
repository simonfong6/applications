#!/usr/bin/env python3
"""
Class
"""
import requests

GREENHOUSE_URL_TEMPLATE = "https://boards.greenhouse.io/{company}"
LEVEL_URL_TEMPLATE = "https://jobs.lever.co/{company}"

TEMPLATES = [GREENHOUSE_URL_TEMPLATE, LEVEL_URL_TEMPLATE]

def normalize(company):
    return company.lower()

def company_on_board(url_template, company):
    url = url_template.format(company=company)
    response = requests.get(url)

    return response.ok

def on_greenhouse(company):
    return company_on_board(GREENHOUSE_URL_TEMPLATE, company)

def on_lever(company):
    return company_on_board(LEVEL_URL_TEMPLATE, company)

def get_careers_page(company):
    career_page_url = None

    company = normalize(company)

    for template in TEMPLATES:
        if company_on_board(template, company):
            career_page_url = template.format(company=company)
            return career_page_url

    return career_page_url

class Class:

    def __init__(self):
        super().__init__()


def main(args):

    check_lever(args.company)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-c', '--company',
                        help="An argument.",
                        type=str,
                        default='default')

    args = parser.parse_args()
    main(args)

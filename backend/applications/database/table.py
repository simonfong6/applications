#!/usr/bin/env python3
"""
Table
"""
import logging

import boto3


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Table:

    def __init__(self,
                 name,
                 region_name='us-west-2',
                 local=None,
                 endpoint=None,
                 port=None):
        super().__init__()

        if local:
            if not endpoint:
                endpoint = 'http://localhost'
            
            if not port:
                port = 8000

            endpoint_url = f'{endpoint}:{port}'
            dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
        else:
            dynamodb = boto3.resource('dynamodb', region_name=region_name)

        self.table = dynamodb.Table(name)

    def put(self, item):
        self.table.put_item(Item=item)
    
    def get(self, key):
        response = self.table.get_item(
            Key=key
        )

        logger.info(f"Response: {response}")

        item = response.get('Item', None)

        return item

    def get_all(self):
        request = self.table.scan()

        items = request['Items']

        return items

    def update(self, key, update_expression, expression_attriubte_values):
        self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attriubte_values
        )

    def delete(self, key):
        response = self.table.delete_item(
            Key=key
        )


def main(args):

    table = Table('companies', local=True, port=8001)

    table.put(
        {
            'name': 'Google',
            'career_link': 'https://google.com/jobs',
        }
    )

    print(table.table.item_count)

    item = table.get(
        key={
            'name': 'Google',
        }
    )
    print(item)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-a', '--arg1',
                        help="An argument.",
                        type=str,
                        default='default')

    args = parser.parse_args()
    main(args)

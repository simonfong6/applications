#!/usr/bin/env python3
"""
DynamoDB
"""
import boto3


class DynamoDB:

    DEFAULT_PROVISIONED_THROUGH_PUT = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    def __init__(self,
                 region_name='us-west-2',
                 local=None,
                 endpoint=None,
                 port=None):
        if local:
            if not endpoint:
                endpoint = 'http://localhost'
            
            if not port:
                port = 8000

            endpoint_url = f'{endpoint}:{port}'
            client = boto3.client('dynamodb', endpoint_url=endpoint_url)
        else:
            client = boto3.client('dynamodb', region_name=region_name)
        self.client = client

    def create_table(
            self,
            table_name,
            key_schema,
            attribute_definitions,
            provisioned_throughput=None):
        
        if not provisioned_throughput:
            provisioned_throughput = DynamoDB.DEFAULT_PROVISIONED_THROUGH_PUT
        
        self.client.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=DynamoDB.DEFAULT_PROVISIONED_THROUGH_PUT
        )

def main():

    dynamo = DynamoDB(local=True, port=8001)
    
    try:
        # Create the DynamoDB table.
        dynamo.create_table(
            table_name='companies',
            key_schema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                },
            ],
            attribute_definitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
            ]
        )

        # Wait until the table exists.
        # table.meta.client.get_waiter('table_exists').wait(TableName='users')

    except dynamo.client.exceptions.ResourceInUseException:
        # do something here as you require
        pass


if __name__ == '__main__':
    main()

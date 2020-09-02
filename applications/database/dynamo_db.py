#!/usr/bin/env python3
"""
DynamoDB
"""
import boto3
from boto3.dynamodb.types import NUMBER


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
            provisioned_throughput=None,
            exists_ok=False):
        
        if not provisioned_throughput:
            provisioned_throughput = DynamoDB.DEFAULT_PROVISIONED_THROUGH_PUT
        
        if exists_ok:
            try:
                self.client.create_table(
                    TableName=table_name,
                    KeySchema=key_schema,
                    AttributeDefinitions=attribute_definitions,
                    ProvisionedThroughput=DynamoDB.DEFAULT_PROVISIONED_THROUGH_PUT
                )
                print(f"Creating table '{table_name}'")
            except self.client.exceptions.ResourceInUseException:
                print(f"Table '{table_name}' exists")
        else:
            self.client.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                ProvisionedThroughput=DynamoDB.DEFAULT_PROVISIONED_THROUGH_PUT
            )
            print(f"Creating table '{table_name}'")

def main():

    dynamo = DynamoDB()
    
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
        ],
        exists_ok=True
    )

    dynamo.create_table(
        table_name='users',
        key_schema=[
            {
                'AttributeName': 'email',
                'KeyType': 'HASH'
            },
        ],
        attribute_definitions=[
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            },
        ],
        exists_ok=True
    )

    dynamo.create_table(
        table_name='jobs',
        key_schema=[
            {
                'AttributeName': 'uuid',
                'KeyType': 'HASH'
            },
        ],
        attribute_definitions=[
            {
                'AttributeName': 'uuid',
                'AttributeType': 'S'
            },
        ],
        exists_ok=True
    )

    dynamo.create_table(
        table_name='users_jobs',
        key_schema=[
            {
                'AttributeName': 'user_uuid',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'uuid',
                'KeyType': 'RANGE'
            },
        ],
        attribute_definitions=[
            {
                'AttributeName': 'user_uuid',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'uuid',
                'AttributeType': 'S',
            },
        ],
        exists_ok=True
    )


if __name__ == '__main__':
    main()

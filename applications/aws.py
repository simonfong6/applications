import boto3

client = boto3.client('dynamodb', region_name='us-west-2')

response = client.put_item(
    TableName='applications',
    Item={
        'applications': 'Google'
    }
)

print(response)

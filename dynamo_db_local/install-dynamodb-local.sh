#!/usr/bin/env bash

DYNAMO_DB_ZIP="dynamodb_local_latest.zip"
DYNAMO_DB_ZIP_URL="https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip"
DYNAMO_DB_DIRECTORY='dynamodb'

# Make the directory, okay if it exists.
mkdir -p $DYNAMO_DB_DIRECTORY
cd $DYNAMO_DB_DIRECTORY

# Download DynamoDB.
curl -s $DYNAMO_DB_ZIP_URL -o $DYNAMO_DB_ZIP

# Unzip it.
unzip $DYNAMO_DB_ZIP

# Remove the zip after downloading it.
rm $DYNAMO_DB_ZIP

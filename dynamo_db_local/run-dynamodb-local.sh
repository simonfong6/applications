#!/usr/bin/env bash
DYNAMO_DB_DIRECTORY='dynamodb'
DYNAMO_DB_LOCAL_PORT="8001"

cd $DYNAMO_DB_DIRECTORY

java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -port $DYNAMO_DB_LOCAL_PORT

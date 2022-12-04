import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

TABLE_NAME = "Movies"
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")
dynamodb=boto3.resource('dynamodb',region_name="us-east-1")
table=dynamodb.Table(TABLE_NAME)
print(table)

response = table.query(KeyConditionExpression=Key('Title').eq('Terminator'))
KeyConditionExpression=Key('Title'),
ExpressionAttributeValues={':Title': 'Rocky'}
print (response["Items"])

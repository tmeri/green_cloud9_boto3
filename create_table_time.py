import boto3
import json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')
print(table.creation_date_time)2
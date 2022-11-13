import json
import boto3

def lambda_handler(event, context):
    client_dynamodb = boto3.resource('dynamodb')
    table = client_dynamodb.Table('Movies')
    Title=event['Title']
            response = table.delete_item(Key={"Title":"Die Hard"})
print(response)
    
  
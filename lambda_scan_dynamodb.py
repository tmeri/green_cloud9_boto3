import boto3    
import json

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("Movies")
    Movies = table.scan() ['Items']
    print(Movies)
    
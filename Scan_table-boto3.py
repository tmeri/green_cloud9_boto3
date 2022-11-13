import boto3 # import boto3 libraries
import json # import json libraries
from boto3.dynamodb.conditions import Key, Attr # add conditions to scanning and querying the table

TABLE_NAME = "Movies" # table name
dynamodb = boto3.resource('dynamodb', region_name="us-east-1") # creating a resource variable
table = dynamodb.Table(TABLE_NAME) 
response = table.scan( # query the table
    FilterExpression=Attr('Title').begins_with('T') & Attr('Genre').eq('Action')
)
items = response['Items'] 
print(items) #print an item from the table




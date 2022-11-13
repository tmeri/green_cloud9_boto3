import boto3
dynamodb = boto3.client('dynamodb') 

response=dynamodb.delete_item(TableName='Movies',
    Key= {
          'Title':{"S": "GoodeFellas"}, # This Item will be deleted
          "Genre": {"S": "Crime"},
    
    }
)
    



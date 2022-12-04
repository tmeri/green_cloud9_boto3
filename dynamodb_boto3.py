import boto3  # Import boto3 which is SDK for Python in AWS IDE

# Get the service resource.
dynamodb = boto3.resource('dynamodb') # Dynamodb variable to call boto3 resource

# Create the DynamoDB table.
table = dynamodb.create_table( # Creating table in DynamoDB in AWS
    TableName='Movies', # Naming table name
    KeySchema=[ # Dynamodb Key-Schema
        {
            'AttributeName': 'Title', # Name of partition key
            'KeyType': 'HASH'# Data type to the partition key
        },
        {
            'AttributeName': 'Genre', # Name of sort key 
            'KeyType': 'RANGE' # Data type of sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Title', # Name of an item
            'AttributeType': 'S' # Defining data type
        },
        {
            'AttributeName': 'Genre', # Name of an item
            'AttributeType': 'S' # Defining data type
        },
    ],
    ProvisionedThroughput={ # The speed of data being read 
        'ReadCapacityUnits': 5, # The speed how quick we want it read and can
        'WriteCapacityUnits': 5 # be changed for faster speed
    }
)

print('Creating Table...')

table.wait_until_exists()   # Wait until the table exists

print(table.item_count)   # Print out some data about the table






            
            
            
            
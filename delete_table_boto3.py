import boto3

client = boto3.client('dynamodb')
client.delete_table(TableName='Movies')
waiter = client.get_waiter('table_not_exists')
waiter.wait(TableName='Movies')
print ("table deleted")

#table.delete()
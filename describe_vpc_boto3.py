import boto3

client=boto3.client('ec2')

x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]

len(no_of_vpcs)

no_of_vpcs

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
x=client.describe_vpcs(Vpc_Id=["vpc-08491928a3ed0fa95"])
    
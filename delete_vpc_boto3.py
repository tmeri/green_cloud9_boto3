import boto3

client=boto3.client('ec2')

client.vpc_delete(VpcId='vpc-050985b9cbf754dde'

)


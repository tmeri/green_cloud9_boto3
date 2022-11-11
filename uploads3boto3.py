#import boto3
#s3 = boto3.resource('s3')
#s3.meta.client.upload_file (r'C:\Users\temes\Desktop\s3_upload_boto3.txt','boto3pythonaws','hello.txt')

import boto3

s3 = boto3.client ('s3')
s3.upload_file ('C:/Users/temes/Desktop/s3_upload_boto3.txt', 'boto3pythonaws', 'teme')
    


#%%

import boto3

def create_apache_ec2(client):
    try:
        client.run_instances(MaxCount=1,
                         MinCount=1,
                         ImageId="ami-09d3b3274b6c5d4aa",
                         InstanceType="t2.micro",
                         KeyName="Dyna-KP",
                         SecurityGroups=["sg-0f351cc36d89de867"],
                         UserData=boot_apache2_script)
        print("Started")
    except:
        print("Failed")
    

#%%
client = boto3.client('ec2')
#%%

boot_apache2_script='''#!/bin/bash
apt update -y
apt upgrade -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''


#%%

create_apache_ec2(client)
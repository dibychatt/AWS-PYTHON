#!/usr/bin/python3
import boto3
import time
import requests
from creds import Creds
from botocore.exceptions import ClientError
from collections import defaultdict

creds = Creds("credentials.csv")
#print("Beware You are doing this activity using this account :" + " " + creds.username)

REGION = "ap-south-1"
ACCESS_KEY = creds.access_key_id
SECRET_KEY = creds.secret_key
ec2 = boto3.resource('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

def get_instance_details():
 running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
 ec2info = defaultdict()
 for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary         
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time
        }
 attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
 for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")
#get_instance_details()

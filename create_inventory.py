#!/usr/bin/python3
import boto3
import time
import sys
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

try:
 os.remove("/data/aws_management/instance_ip", "/data/aws_management/instance_id")
except Exception:
 pass

def find_master_or_slave():
 running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
 with open('/data/aws_management/instance_ip', 'w') as f:
  for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
        if tag['Value'] == 'SLAVE':
             instance_ips = (instance.public_ip_address)
             print(instance_ips, file=f)
#find_master_or_slave()

def find_instance_ID_of_slave():
 running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
 with open('/data/aws_management/instance_id', 'w') as f:
  for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
        if tag['Value'] == 'SLAVE':
             instance_ips = (instance.instance_id)
             print(instance_ips, file=f)
#find_instance_ID_of_slave()


#!/usr/bin/python3
import boto3
import boto3.ec2
import time
from creds import Creds
from botocore.exceptions import ClientError

creds = Creds("credentials.csv")
#print("Beware You are going to do the activity using this account :" + " " + creds.username)

REGION = "ap-south-1"
ZONE = "ap-south-1a"
ACCESS_KEY = creds.access_key_id
SECRET_KEY = creds.secret_key
ec2 = boto3.client('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

def create_volume():
 try:
  with open('/data/aws_management/instance_id', 'r') as file:
   counter = 0
   content = file.read()
   list = content.split('\n')
  for id in list:
   if id:
    counter += 1
    print("Your volume is getting created..")
    time.sleep(2)
    create = ec2.create_volume(AvailabilityZone = ZONE, Size = 10, VolumeType = 'gp2')
    volume_id = create['VolumeId']
    print("Your volume is ready")
    print("Volume ID is", volume_id)
    print("Lets attach this volume to your instances...")
    time.sleep(10)
    attach = ec2.attach_volume(Device = '/dev/xvdf', InstanceId = id, VolumeId = volume_id)
    print("Your volume", volume_id + " " "is attached to" + " " + id)
  time.sleep(1)
 except:
   pass
#create_volume()


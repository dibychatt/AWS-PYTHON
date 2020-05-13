#!/usr/bin/python3
import boto3
import time
from creds import Creds
from botocore.exceptions import ClientError

creds = Creds("credentials.csv")
print("Beware You are doing this activity using this account :" + " " + creds.username)

REGION = "ap-south-1"
ACCESS_KEY = creds.access_key_id
SECRET_KEY = creds.secret_key
ec2 = boto3.client('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

image_id = "ami-0f0a1a6780c08ab89"
instance_type = "t2.micro"
keypair_name = "automation"
SECURITY_GROUP = "sg-0ffc7b020b640c5f0"
IAM_PROFILE = "RoleforAutomation"
response = {}

def provision_server():
  global InstanceId
  try:
   response = ec2.run_instances(ImageId=image_id,
   InstanceType=instance_type,
   KeyName=keypair_name,
   SecurityGroupIds=[SECURITY_GROUP],
   IamInstanceProfile={'Name': IAM_PROFILE}, MinCount=1, MaxCount=1)
   print("Provisioning instance…")
   time.sleep(5)
   print("Your instance is ready...")
   print("Your Instance ID is : " + " " + str(response['Instances'][0]['InstanceId']))
   InstanceId = (str(response['Instances'][0]['InstanceId']))
  except ClientError as e:
   print(e)
#provision_server()

def add_instance_name():
 print("Adding Instance name as SLAVE..")
 ec2.create_tags(Resources=[InstanceId], Tags=[{'Key':'Name', 'Value':'SLAVE'}])
 print("Tag added..")
#add_instance_name()

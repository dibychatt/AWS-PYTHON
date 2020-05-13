#!/usr/bin/python3
import boto3
import time
from creds import Creds
from botocore.exceptions import ClientError

creds = Creds("credentials.csv")
#print("Beware You are going to do the activity using this account :" + " " + creds.username)

REGION = "ap-south-1"
ACCESS_KEY = creds.access_key_id
SECRET_KEY = creds.secret_key
ec2 = boto3.resource('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)
in_file = open('/data/aws_management/instance_id', 'r')

def instance_ids():
 global id
 confirm = input("what action you want to perform on instances..? (start/stop/reboot/terminate) : ")
 for id in in_file:
  id = id.strip()
  if confirm == 'terminate':
   terminate_instance()
  if confirm == 'stop':
   stop_instance()
  if confirm == 'start':
   start_instance()
  if confirm == 'reboot':
   reboot_instance()

def terminate_instance():
 try:
   time.sleep(2)
   print("Terminating instance :", id)
   instance = ec2.Instance(id)
   instance.terminate()
   print("Instance" + " " + id + " " + "is terminated")
   time.sleep(1)
 except:
  pass

def stop_instance():
 try:
   time.sleep(2)
   print("Stopping instance :", id)
   instance = ec2.Instance(id)
   instance.stop()
   print("Instance" + " " + id + " " + "is stopped")
   time.sleep(1)
 except:
  pass

def start_instance():
 try:
   time.sleep(2)
   print("Starting instance :", id)
   instance = ec2.Instance(id)
   instance.start()
   print("Instance" + " " + id + " " + "is started")
   time.sleep(1)
 except:
  pass

def reboot_instance():
 try:
   time.sleep(2)
   print("Rebooting instance :", id)
   instance = ec2.Instance(id)
   instance.reboot()
   print("Instance" + " " + id + " " + "is Rebooted")
   time.sleep(1)
 except:
  pass

#instance_ids()

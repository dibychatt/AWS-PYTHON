#!/usr/bin/python3
#!/usr/bin/msfconsole
import os
import time
from pick import pick
import instance_creation as f1
import list_instance as f2
import create_inventory as f3
import initial_setup as f4
import create_attach_volume as f5
import manage_instance as f6

title = 'Please choose your action: '
options = ['Create-new-instance', 'View-deployed-instance', 'Initial-setup-on-deployed-instance', 'Create-attach-volume', 'Run-all(1.Deploy, 2.View, 3.Create-and-Attachvolume, 4.Initialsetup)', 'Manage-instances(Start/stop/reboot/terminate)']
option, index = pick(options, title)

def main():
 if index == 0:
  print('-------------')
  print("You have selected to perform : ", (option))
  x = int(input ("How many instance you want to provision : "))
  for i in range(x):
   print("Deploying instance", i)
   f1.provision_server()
   f1.add_instance_name()
  print('-------------') 

 if index == 1:
   print('-------------')
   print("You have selected to perform : ", (option))
   f2.get_instance_details()
   print('-------------')

 if index == 2:
   print('-------------')
   print("You have selected to perform : ", (option))
   print("Preparing your host inventory file....")
   time.sleep(3)
   f3.find_master_or_slave()
   f3.find_instance_ID_of_slave()
   print("Lets start pushing setup to new instance....")
   time.sleep(3)
   f4.enable_connection()
   print('-------------')
  
 if index == 3:
   print('-------------')
   print("You have selected to perform : ", (option))
   print("Preparing your host inventory file....")
   time.sleep(3)
   f3.find_master_or_slave()
   f3.find_instance_ID_of_slave()
   print("If you wish to create & attaching volume - makesure your instance is in Zone : ap-south-1a")
   print("Lets start creating volume and attach it to instances....")
   time.sleep(3)
   f5.create_volume()
   print('-------------')
 
 if index == 4:
   print('-------------')
   print("You have selected to perform : ", (option))
   print("Step 1 : Creating new instance")
   x = int(input ("How many instance you want to provision : "))
   for i in range(x):
    print("Deploying instance", i)
    f1.provision_server()
    f1.add_instance_name()
   time.sleep(40)
   print('-------------')
   print("Step 2 : Listing all running machines in your account")
   f2.get_instance_details()
   print('-------------')
   time.sleep(15)
   print("Step 3 : Create host inventory file")
   time.sleep(3)
   f3.find_master_or_slave()
   f3.find_instance_ID_of_slave()
   print('-------------')
   time.sleep(10)
   print("If you wish to create & attaching volume - makesure your new instance is in Zone : ap-south-1a")
   time.sleep(10)
   answer = input ("Do you wish to continue with create & attach volume ? (yes/no) : ")
   if answer == 'yes':
    print("Step 4 : Creating volume and attach")
    f5.create_volume()
    print("Step 5 : Pushing Initial setup to newly deployed machine")
    f4.enable_connection()
   else:
    print("Step 4 : Pushing Initial setup to newly deployed machine")
    f4.enable_connection()
   print('-------------')
 
 if index == 5:
  print('-------------')
  print("You have selected to perform : ", (option))
  print("Step 1 : Create host inventory file")
  f3.find_master_or_slave()
  f3.find_instance_ID_of_slave()
  print("Step 2 : Lets perform the task you want..")
  f6.instance_ids()
  print('-------------')

main()

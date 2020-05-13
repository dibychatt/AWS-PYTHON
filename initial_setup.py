#!/usr/bin/python3
import paramiko
import time
import sys

in_file = open('/data/aws_management/instance_ip', 'r')
login_id = 'ec2-user'
login_key = paramiko.RSAKey.from_private_key_file('/data/aws_management/automation.pem')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def enable_connection():
 for host in in_file:
    host=host.strip()
    print('Connecting to', host)
    ssh.connect(host, username=login_id, pkey=login_key)
    time.sleep(2)
    print('connected')
    time.sleep(2)
    print("---------")
    install_package()
    print("---------")
    copy_files()
    print("---------")
    post_copy_changes()
    print("---------")
    ngrok_token_install()
    print("---------")
    execute_scripts()
    print("---------")
 ssh.close()

def install_package():
 try:
   print('Step 1 : Package Installation started')
   commands = ["sudo yum install httpd* -y", "sudo yum install python3 -y", "sudo pip3 install boto3", "sudo pip3 install paramiko", "sudo chmod -R 777 /data"] 
   for command in commands:
     print("Executing {}".format(command))
     stdin, stdout, stderr = ssh.exec_command(command)
     exit_status = stdout.channel.recv_exit_status()
     if exit_status == 0:
        print("Command executed successfully")
     else:
        print("Command failed to execute")
   print('Package Installation completed')
 except:
  pass

def copy_files():
 try:
  print('Step 2 : File copy started')
  files = ['/data/ngrok', '/data/hack.py', '/data/create-apk.py', '/data/exploit.sh', '/data/start-ngrok-multi-port.py', '/data/start-ngrok-single-port.py', '/data/metasploit.py', '/data/swap_creation.sh']
  for file in files:
   print("copying {}".format(file))
   destination = file
   sftp = ssh.open_sftp()
   sftp.put(file, destination)
   sftp.close()
  print('File copy ended')
  print(stderr.read())
 except:
  pass

def post_copy_changes():
 try:
   print('Step 3 : Post copy changes started')
   commands = ["sudo chmod +x /data/*", "sudo service httpd start"]
   for command in commands:
     print("Executing {}".format(command))
     stdin, stdout, stderr = ssh.exec_command(command)
     exit_status = stdout.channel.recv_exit_status()
     if exit_status == 0:
        print("Command executed successfully")
     else:
        print("Command failed to execute")
   print('Post copy changes completed')
 except:
  pass

def ngrok_token_install():
 try:
  print('Step 4 : Ngrok token installation started')
  commands = ["sudo /data/ngrok authtoken 1aiQZXY9XWixN4AjfQ00q58b9v5_2iXjDxDCy7yWBBemE9Asd"]
  for command in commands:
     print("Executing {}".format(command))
     stdin, stdout, stderr = ssh.exec_command(command)
     exit_status = stdout.channel.recv_exit_status()
     if exit_status == 0:
        print("Command executed successfully")
     else:
        print("Command failed to execute")
  print('Ngrok token installation completed')
 except:
  pass

def execute_scripts():
 try:
  print('Step 5 : Scripts executions in remote server')
  commands = ['sudo /data/metasploit.py', 'sudo /data/start-ngrok-single-port.py', 'sudo /data/swap_creation.sh']
  for command in commands:
     print("Executing script {}".format(command))
     stdin, stdout, stderr = ssh.exec_command(command)
     exit_status = stdout.channel.recv_exit_status()
     if exit_status == 0:
        print("Script executed successfully")
     else:
        print("Script execution failed")
  print('Scripts executed in remote server')
 except:
  pass

#enable_connection()

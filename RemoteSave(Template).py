# This script will allow you to save data from a test to a remove server on your network
# Default file saved = LocalInfo.txt
# Default saved location = 'C:/Users/admin/Desktop/SHARE/LocalInfo.txt'
# Update your IP Address, LogInName and Password for the remote server


import socket
import os
import shutil
import paramiko

# Get the computer name and IP
computer_name = socket.gethostname()
ip_address = socket.gethostbyname(computer_name)

# Log the information to a text file
with open('LocalInfo.txt', 'w') as file:
    file.write(f'Computer Name: {computer_name}\n')
    file.write(f'IP Address: {ip_address}\n')

# Connect to the remote computer using SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.100.xxx.xx', username='LogInName', password='Password')

# Copy the LocalInfo.txt file to the remote computer
sftp = ssh.open_sftp()
sftp.put('LocalInfo.txt', 'C:/Users/admin/Desktop/SHARE/LocalInfo.txt')
sftp.close()

# Close the SSH connection
ssh.close()


"""
Notes:

Make sure OpenSSF Server is installed and running:

Open the Start menu and search for "Settings".
Click on "Apps" and then select "Optional features".
Click on "Add a feature" and then scroll down and select "OpenSSH Server".
Click on "Install" and wait for the installation process to complete.
Once the installation is complete, you can open the Command Prompt or PowerShell and run the following command to start the SSH service:
Open CMD (as Adminsitartor)> net start sshd


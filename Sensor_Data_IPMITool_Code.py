# Read sensor data from Redfish
# Add IP Address, LoginName and Password
# Must have ipmitool.exe in base folder thefile.cng to work


import subprocess

command = 'ipmitool.exe -H 10.100.xxx.xx -U LoginName -P Password sensor'
#                           \---Add---/     \--Add--/   \--Add--/

try:
    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))
except subprocess.CalledProcessError as e:
    print(f"Command execution failed with error code {e.returncode}")

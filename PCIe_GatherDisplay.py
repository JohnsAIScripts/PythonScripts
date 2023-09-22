import subprocess

# TITLE
print("")
print("===== PCIe TEST =====")
print("")


# Define the command to retrieve PCIe card information
command = ['wmic', 'path', 'win32_pnpsigneddriver', 'get', 'devicename', 'classguid', '/format:list']

# Run the command and capture the output
output = subprocess.check_output(command)

# Convert the output from bytes to a string
output_str = output.decode()

# Split the output into individual devices
devices = output_str.split('\n\n')

# Loop through each device and print its information
for device in devices:
    print(device)

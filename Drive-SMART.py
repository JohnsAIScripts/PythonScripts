import subprocess

def get_smart_data(drive):
    try:
        # Specify the full path to the smartctl executable
        smartctl_path = r'C:\Program Files\smartmontools\bin\smartctl.exe'  # Replace with the actual path
        
        # Define the smartctl command
        command = [smartctl_path, '-a', drive]
        
        # Run the command and capture the output
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    drive = 'C:'  # Replace with the appropriate drive letter for your system
    
    smart_data = get_smart_data(drive)
    if smart_data:
        print("SMART Data:")
        print(smart_data)
    else:
        print(f"Failed to retrieve SMART data for drive {drive}.")

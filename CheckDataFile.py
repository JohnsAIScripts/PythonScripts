# REAL-TIME Check for a string anywhere in a file.
# The sting dictates what to do next.
# "Power" = break
# "Checking" = Keep checking
# No data = END


import os
import time

file_path = "C:/Users/Admin/Desktop/AI-Scripts/LocalData/PowerCycle.txt"

while True:
    print("Checking contents of PowerCycle.txt")
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            contents = f.read()
            if "Power" in contents:
                # Power cycle the computer here (not recommended)
                print("Power cycling the computer")
                break
            elif "Checking" in contents:
                time.sleep(20)
                continue
            elif "" in contents:
                # No data in the file
                print("Your file is empty - END")
                break
    else:
        time.sleep(20)

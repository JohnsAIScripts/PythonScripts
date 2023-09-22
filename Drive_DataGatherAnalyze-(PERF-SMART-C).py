import psutil
import time
import os

# Set the number of 1MB chunks to write/read
num_chunks = 10

import subprocess

# Define the command to retrieve SMART data
command = ['smartctl', '-a', 'C:']

# Run the command and capture the output
output = subprocess.check_output(command)

# Print the output
print(output.decode())

# Open a file for writing
with open('C:/testfile', 'wb') as f:
    # Iterate over the chunks and write them to disk
    for i in range(num_chunks):
        # Calculate the offset based on the chunk index
        offset = i * 1024 * 1024
        # Seek to the offset
        f.seek(offset)
        # Generate some random data to write
        data = bytearray(os.urandom(10000 * 10000))
        # Measure the start time
        start_time = time.monotonic()
        # Write the data to disk
        f.write(data)
        # Measure the end time
        end_time = time.monotonic()
        # Print the elapsed time
        print(f"Write chunk {i}: {end_time - start_time:.3f} seconds")

# Open the file for reading
with open('C:/testfile', 'rb') as f:
    # Iterate over the chunks and read them from disk
    for i in range(num_chunks):
        # Calculate the offset based on the chunk index
        offset = i * 1024 * 1024
        # Seek to the offset
        f.seek(offset)
        # Measure the start time
        start_time = time.monotonic()
        # Read the data from disk
        data = f.read(10000 * 10000)
        # Measure the end time
        end_time = time.monotonic()
        # Print the elapsed time
        print(f"Read chunk {i}: {end_time - start_time:.3f} seconds")

# Delete the test file
os.remove('C:/testfile')


"""
This script writes and reads 100 10MB chunks of random data to and
from the file 'testfile', and prints out the elapsed time for each
operation. You can modify the num_chunks variable to control how
many chunks to write/read. Note that the script will create a file
named 'testfile' in the current working directory and delete it
after the script completes.
"""

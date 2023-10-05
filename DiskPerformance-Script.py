import time
import os

# TITLE
print("")
print("===== DISK PERFORMANCE TEST =====")
print("")

# Define the different sizes of data to be read and written
sizes = [1024000, 4096000, 16384000, 32123000, 65536000, 128321000, 262144000, 512144000, 1062144000]

# Define the path to the file to be used for the test
test_file_path = "C:/disk_test.txt"

# Define the number of iterations for each size
iterations = 10

# Function to measure the time it takes to write a given amount of data to the file
def write_test(size):
    with open(test_file_path, "wb") as f:
        data = os.urandom(size)
        start_time = time.monotonic()
        for i in range(iterations):
            f.write(data)
        end_time = time.monotonic()
        return end_time - start_time

# Function to measure the time it takes to read a given amount of data from the file
def read_test(size):
    with open(test_file_path, "rb") as f:
        start_time = time.monotonic()
        for i in range(iterations):
            f.read(size)
        end_time = time.monotonic()
        return end_time - start_time

# Perform the test for each size and print the results
for size in sizes:
    write_time = write_test(size)
    read_time = read_test(size)
    WMB = size / (write_time+0.0000001) / 100000
    RMB = size / (read_time+0.0000001) /100000
    MBSize = size / 100000
    # print(f"Size: {MBSize} MB | Write time: {write_time:.6f} seconds | Read time: {read_time:.6f} seconds | WRITE: {WMB:.0f} MB/s | READ: {RMB:.0f} MB/s")
    print(f"Size: {MBSize} MB | WRITE: {WMB:.0f} MB/s | READ: {RMB:.0f} MB/s")

# Remove the test file
os.remove(test_file_path)

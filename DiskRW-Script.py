import os
import random

# TITLE
print("")
print("===== DISK READ/WRITE TEST =====")
print("")


# Define the size of the file to be written and read
file_size = 1024 * 1024 * 100  # 100 MB

# Define the file name and path
file_path = "test_file.bin"

# Generate random data to be written to the file
data = bytearray(random.getrandbits(8) for _ in range(file_size))

# Write the data to the file
with open(file_path, "wb") as f:
    f.write(data)

# Read the data back from the file and check for errors
with open(file_path, "rb") as f:
    read_data = f.read()
    if read_data != data:
        print("Read/write test failed: data mismatch!")
    else:
        print("Read/write test passed!")

# Remove the file
os.remove(file_path)

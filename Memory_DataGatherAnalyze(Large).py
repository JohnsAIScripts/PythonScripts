import time

# TITLE
print("")
print("===== MEMORY DATA GATHER (large) TEST =====")
print("")

# Set the chunk size to 10MB
chunk_size = 100 * 1024 * 1024

# Allocate a chunk of memory to write to
data = bytearray(chunk_size)

# Measure the write performance
start_time = time.monotonic()
for i in range(chunk_size):
    data[i] = i % 256
end_time = time.monotonic()

# Print the write performance
print(f"Wrote {chunk_size} bytes in {end_time - start_time:.3f} seconds ({chunk_size / (end_time - start_time) / 1024 / 1024:.2f} MB/s)")

# Measure the read performance
start_time = time.monotonic()
for i in range(chunk_size):
    val = data[i]
end_time = time.monotonic()

# Print the read performance
print(f"Read {chunk_size} bytes in {end_time - start_time:.3f} seconds ({chunk_size / (end_time - start_time) / 1024 / 1024:.2f} MB/s)")



"""
This script first allocates a 10MB chunk of memory to write to,
and then performs a sequential write operation by iterating over
the memory and writing a byte at each index. It then measures the
time it takes to complete the write operation and prints out the
write performance in MB/s. Finally, the script performs a sequential
read operation by iterating over the memory again and reading a byte
at each index. It measures the time it takes to complete the read
operation and prints out the read performance in MB/s.
"""

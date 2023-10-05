import time

# TITLE
print("")
print("===== MEMORY PERFORMANCE TEST =====")
print("")

data = b'\0' * 2_000_000_000  # Create a 10MB byte string of zeros

# Write the data to memory and measure the time it takes
start_time = time.monotonic()+0.0001
with open('test_file_path', 'wb') as f:
    f.write(data)
end_time = time.monotonic()
write_speed = len(data) / (end_time - start_time)

# Read the data from memory and measure the time it takes
start_time = time.monotonic()
with open('test_file_path', 'rb') as f:
    f.read(len(data))
end_time = time.monotonic()+0.00001
read_speed = len(data) / (end_time - start_time)

print(f"Write speed: {write_speed / 1_000_000:.2f} MB/s")
print(f"Read speed: {read_speed / 1_000_000:.2f} MB/s")

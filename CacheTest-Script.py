import time

# TITLE
print("")
print("===== CACHE TEST =====")
print("")

# Define the size of the cache to be tested
cache_size = 1024 * 1024  # 1 MB

# Allocate memory for the cache
cache = bytearray(cache_size)

# Initialize the cache with random data
for i in range(cache_size):
    cache[i] = i % 4
    print("             cache")
    print(i)

# Test the cache by repeatedly accessing the data in the cache
start_time = time.monotonic()
for i in range(3):
    for j in range(cache_size):
        value = cache[j]
        cache[j] = value
        print("                    value")
        print(j)
end_time = time.monotonic()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the results
print(f"Cache test completed in {elapsed_time:.3f} seconds")

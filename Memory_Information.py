import psutil

print("")
print("===== Memory Information =====")
print("")
        
def get_memory_info():
    try:
        memory_info = {}
        
        # Get memory usage information
        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        
        memory_info["Total RAM (bytes)"] = virtual_memory.total
        memory_info["Available RAM (bytes)"] = virtual_memory.available
        memory_info["Used RAM (bytes)"] = virtual_memory.used
        memory_info["Free RAM (bytes)"] = virtual_memory.free
        
        memory_info["Total Swap Space (bytes)"] = swap_memory.total
        memory_info["Used Swap Space (bytes)"] = swap_memory.used
        memory_info["Free Swap Space (bytes)"] = swap_memory.free
        
        return memory_info
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    memory_info = get_memory_info()
    if memory_info:
        print("Memory Information:")
        for key, value in memory_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve memory information.")

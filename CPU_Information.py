import psutil
#import cpuinfo
import os
import platform

def get_cpu_info():
    try:
        cpu_info = {}
        
        #info = cpuinfo.get_cpu_info()
        #cpu_info["Processor Name"] = info["brand_raw"]
        #cpu_info["Cache"] = info["l3_cache_size"]
        # Get base and actual CPU frequency using cpuinfo
        #cpu_info["Base Frequency (MHz)"] = info["hz_actual_friendly"]

        # Get general CPU information using psutil
        cpu_info["Model"] = platform.processor()
        cpu_info["Cores"] = psutil.cpu_count(logical=False)
        cpu_info["Threads"] = psutil.cpu_count(logical=True)
        cpu_info["Frequency"] = psutil.cpu_freq(percpu=True)
        
        return cpu_info
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    cpu_info = get_cpu_info()
    if cpu_info:
        print("")
        print("===== CPU Information =====")
        print("")
        for key, value in cpu_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve CPU information.")



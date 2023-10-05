import subprocess

scripts = ["CPU_Information.py",
    "DiskPerformance-Script.py",
    "DiskRW-Script.py",
    "Drive_DataGatherAnalyze-(PERF-SMART-C).py",
    "Memory_Information.py",
    "Memory_DataGatherAnalyze3.py",
    "Memory_DataGatherAnalyze4.py",
    "MemoryPerformance-Script.py",
    "Network_DataGatherAnalyze.py"   
]

#for filepath in filepaths:
#    subprocess.call(["python", filepath])

output_file = "MultiTest.txt"

with open(output_file, "w") as file:
    for script in scripts:
        file.write(f"Output for {script}:\n")
        result = subprocess.call(["python", script], stdout=file, stderr=file)
        file.write("\n")

print(f"All scripts executed. Output saved to '{output_file}'.")

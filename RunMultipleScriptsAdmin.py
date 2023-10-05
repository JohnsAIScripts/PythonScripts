###############################################
# Launch all HRO Benchmark Suites             # 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~             #
#                                             #
# Pre-requisits:                              #
#  - Updage__python-3.10.9-amd64              #
#  - Update__smartmontools-7.3-1.win32-setup  #
#  - pip install -r requirements              #
###############################################


import subprocess
number = 1
print("")

scripts = ["Drive-SMART.py",
    "DiskPerformance-Script.py",
    "Memory_DataGatherAnalyze(Small).py",
    "Memory_DataGatherAnalyze(Large).py",
    "MemoryPerformance-Script.py"
]

#for filepath in filepaths:
#    subprocess.call(["python", filepath])

output_file = "HRO_TEST_SUMMARY.txt"

with open(output_file, "w") as file:
    for script in scripts:
        print(f" Test {number} of 5 in progress. ({script})")
        # file.write(f"Output for {script}:\n")
        result = subprocess.call(["python", script], stdout=file, stderr=file)
        file.write("\n")
        number += 1

print("")
print(f"All scripts executed. Output saved to '{output_file}'.")
print("")


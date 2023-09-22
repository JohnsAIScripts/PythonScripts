import re
import numpy as np
import matplotlib.pyplot as plt

# Read data from the text file
with open('ChartThis2.txt', 'r') as file:
    data = file.read()

# Extract write and read speeds using regular expressions
write_speeds = re.findall(r'Write speed(\d+): ([\d.]+) MB/s', data)
read_speeds = re.findall(r'Read speed(\d+): ([\d.]+) MB/s', data)

# Sort the speeds based on group number
write_speeds = sorted([(int(group), float(speed)) for group, speed in write_speeds])
read_speeds = sorted([(int(group), float(speed)) for group, speed in read_speeds])

# Separate the group numbers and speeds
write_groups, write_values = zip(*write_speeds)
read_groups, read_values = zip(*read_speeds)

# Create bar graphs for write speeds
plt.bar(write_groups, write_values, width=0.4, align='center', label='Write Speed')

# Create bar graphs for read speeds
plt.bar(np.array(read_groups) + 0.4, read_values, width=0.4, align='center', label='Read Speed')

plt.xlabel('Group')
plt.ylabel('Speed (MB/s)')
plt.title('Write and Read Speeds by Group')
plt.legend()

plt.xticks(range(1, len(write_groups) + 1))
plt.grid(True)
plt.show()

import csv
import random

# CREATE RANDOM DATA

labels = ['pass', 'fail', 'tbd', 'na']
data = [(i, random.choice(labels), random.randint(40, 60)) for i in range(1, 101)]

with open('random_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Label', 'Data', 'Value'])
    for i in range(1, 101):
        writer.writerow([f'Test Case {i}', random.choice(labels), "1"])



# CHART RANDOM DATA

import csv
import matplotlib.pyplot as plt

# Open the file and read its contents
with open('random_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data_counts = {}
    for row in reader:
        data_value = row['Data']
        if data_value in data_counts:
            data_counts[data_value] += 1
        else:
            data_counts[data_value] = 1

# Convert the data_counts dictionary into two lists
data_labels = []
data_values = []
for key, value in data_counts.items():
    data_labels.append(key)
    data_values.append(value)

# Plot the data as a pie chart
plt.pie(data_values, labels=data_labels)
plt.title('Data Counts')
plt.show()



# Create graph of data - no sorting or summing
"""
import csv
import matplotlib.pyplot as plt

# read data from csv file
with open('random_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip header row
    labels = []
    data = []
    for row in csv_reader:
        labels.append(row[1])
        data.append(int(row[2]))

# create pie chart
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct='%1.1f%%')
ax.set_title('Random Data Pie Chart')

# show chart
plt.show()
"""

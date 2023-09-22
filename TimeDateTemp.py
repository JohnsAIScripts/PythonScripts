import datetime

# Get current time and date
now = datetime.datetime.now()

# Read the temperature from a file (assuming the temperature is stored in a file named "temp.txt")
with open("temp.txt", "r") as file:
    temp = file.read().strip()

# Write the time, date, and temperature to the log file
with open("TimeDateTemp.log", "a") as file:
    file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Temperature: {temp}°C\n")

print("Time, date, and temperature logged to TimeDateTemp.log")

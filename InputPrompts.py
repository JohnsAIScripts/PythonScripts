
# Prompt the user to input their name, age, and goal
name = input("What is your name? ")
age = input("What is your age? ")
goal = input("What is your goal? ")

# Write the user's information to a text file
with open("user_info2.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Goal: {goal}\n")

# Confirm that the information was written to the file
print("User information written to file.")

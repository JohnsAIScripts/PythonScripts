# copy column F (lines 5-122) from all csv files in folder Perf_RESULTS to a
# single file called Perf_RESULTS.csv)


import os
import pandas as pd

# Define the folder containing CSV files
folder_path = "Perf_RESULTS"

# Create an empty DataFrame to store the concatenated data
combined_data = pd.DataFrame()

# Loop through all CSV files in the folder except "Data.csv"
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv") and file_name != "Data.csv":
        # Load the CSV file
        file_path = os.path.join(folder_path, file_name)
        dataset_data = pd.read_csv(file_path, usecols=[5], header=None, skiprows=5, nrows=117)

        # Rename the column to the dataset name (without the .csv extension)
        dataset_name = os.path.splitext(file_name)[0]
        dataset_data.rename(columns={5: dataset_name}, inplace=True)

        # Concatenate the dataset data to the combined_data DataFrame
        combined_data = pd.concat([combined_data, dataset_data], axis=1)

# Save the combined data to a new CSV file
output_file = os.path.join(folder_path, "Perf_RESULTS.csv")
combined_data.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")

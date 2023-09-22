import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Read the data from the CSV file
data = pd.read_csv('data8.csv')

# Fit the linear regression model
X = data['A'].values.reshape(-1, 1)
y = np.arange(1, len(X) + 1)

regressor = LinearRegression()
regressor.fit(X, y)

# Calculate the prediction and average
prediction = regressor.predict([[len(X) + 1]])
average = np.mean(data['A'])

# Print the results
print(f"Prediction: {prediction[0]}")
print(f"Average: {average}")


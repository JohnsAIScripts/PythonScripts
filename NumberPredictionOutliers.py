import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


# Read the data from the CSV file
data = pd.read_csv('data8.csv')

# Initialize empty lists to store outliers and inliers
outliers = []
inliers = []

# Iterate over the data and identify outliers
for i in range(len(data)):
    current_value = data['A'].iloc[i]
    prev_value = data['A'].iloc[i-1] if i > 0 else None
    next_value = data['A'].iloc[i+1] if i < len(data)-1 else None
    
    if prev_value is not None and abs(current_value - prev_value) > abs(0.5 * prev_value):
        outliers.append(current_value)
    elif next_value is not None and abs(current_value - next_value) > abs(0.5 * next_value):
        outliers.append(current_value)
    else:
        inliers.append(current_value)

# Print the outliers, if any
if len(outliers) > 0:
    print("Outliers found:")
    print(outliers)
else:
    # Fit the linear regression model using inliers
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

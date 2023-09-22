import pandas as pd
from prophet import Prophet
import numpy as np

# Specify the file path
file_path = 'data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Sort the DataFrame by date in ascending order
df.sort_values('date', inplace=True)

# Perform time series forecasting using Prophet
model = Prophet()
model.fit(df[['date', 'value']].rename(columns={'date': 'ds', 'value': 'y'}))

# Make predictions for future dates
future_dates = model.make_future_dataframe(periods=365)
forecast = model.predict(future_dates)

# Detect anomalies based on a value difference of more than 7%
df['yhat'] = forecast['yhat']
df['residual'] = np.abs(df['value'] - df['yhat'])
median_abs_deviation = np.median(df['residual'])
threshold = 0.07 * np.median(df['value'])
df['anomaly'] = df['residual'] > threshold

# Print the detected anomalies
anomalies = df[df['anomaly']]
print("Detected anomalies:")
if len(anomalies) == 0:
    print("No anomalies detected.")
else:
    for index, row in anomalies.iterrows():
        print("Date:", row['date'])
        print("Value:", row['value'])
        print()

# Predict the next anomaly occurrence
last_date = df['date'].iloc[-1]
next_date = last_date + pd.DateOffset(days=1)
next_value = model.predict(pd.DataFrame({'ds': [next_date]}))['yhat'].values[0]

print("Next anomaly prediction:")
print("Date:", next_date)
print("Predicted Value:", next_value)

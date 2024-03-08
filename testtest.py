import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset (replace 'data.csv' with your data file)
data = pd.read_csv('data.csv')

# Split data into features (X) and target variables (y)
X = data[['Feature1', 'Feature2', ...]]  # Features influencing Availability, Performance, and Quality
y_availability = data['Availability']  # Target variable for Availability
y_performance = data['Performance']  # Target variable for Performance
y_quality = data['Quality']  # Target variable for Quality

# Split data into training and testing sets
X_train, X_test, y_availability_train, y_availability_test, y_performance_train, y_performance_test, y_quality_train, y_quality_test = train_test_split(X, y_availability, y_performance, y_quality, test_size=0.2, random_state=42)

# Create linear regression models for each component
model_availability = LinearRegression()
model_performance = LinearRegression()
model_quality = LinearRegression()

# Train the models
model_availability.fit(X_train, y_availability_train)
model_performance.fit(X_train, y_performance_train)
model_quality.fit(X_train, y_quality_train)

# Predict components for testing data
y_availability_pred = model_availability.predict(X_test)
y_performance_pred = model_performance.predict(X_test)
y_quality_pred = model_quality.predict(X_test)

# Evaluate the models
mse_availability = mean_squared_error(y_availability_test, y_availability_pred)
mse_performance = mean_squared_error(y_performance_test, y_performance_pred)
mse_quality = mean_squared_error(y_quality_test, y_quality_pred)

print('Mean Squared Error for Availability:', mse_availability)
print('Mean Squared Error for Performance:', mse_performance)
print('Mean Squared Error for Quality:', mse_quality)
import matplotlib.pyplot as plt

# Plot histograms for Availability, Performance, and Quality predictions
plt.figure(figsize=(10, 8))

# Histogram for Availability
plt.subplot(3, 1, 1)
plt.hist(y_availability_pred, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Availability')
plt.ylabel('Frequency')
plt.title('Histogram of Availability Predictions')

# Histogram for Performance
plt.subplot(3, 1, 2)
plt.hist(y_performance_pred, bins=10, color='green', edgecolor='black', alpha=0.7)
plt.xlabel('Performance')
plt.ylabel('Frequency')
plt.title('Histogram of Performance Predictions')

# Histogram for Quality
plt.subplot(3, 1, 3)
plt.hist(y_quality_pred, bins=10, color='red', edgecolor='black', alpha=0.7)
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.title('Histogram of Quality Predictions')

plt.tight_layout()
plt.show()

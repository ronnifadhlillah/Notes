from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

data = {
    'humPercent': [75, 58, 55, 78, 63, 62, 62, 59, 78, 58, 76, 78, 83, 72],
    'windSpeedKmh': [6, 22, 17, 5, 4, 6, 10, 11, 20, 4, 21, 10, 21, 17],
    'tempC': [22, 23, 34, 23, 22, 25, 24, 31, 30, 33, 24, 24, 25, 28]
}

df = pd.DataFrame(data)


# Separating feature (X) and target (y)
X = df[['humPercent', 'windSpeedKmh']]
y = df['tempC']

# Splitting data into training Data and Test Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train liner regresssion model
model = LinearRegression()
model.fit(X_train, y_train)

# Perform predictions on the test data.
y_pred = model.predict(X_test)

# Model perform evaluation
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Prediction for new data (Example: Humidity 90%, Wind Speed 17 km/h)
newData = np.array([[90, 17]])
tempPredicition = model.predict(newData)
print(f"New temp prediction: {tempPredicition[0]:.2f} °C")

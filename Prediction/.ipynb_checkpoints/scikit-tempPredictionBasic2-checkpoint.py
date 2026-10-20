from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd

data = {
    'humPercent': [75, 58, 55, 78, 63, 62, 62, 59, 78, 58, 76, 78, 83, 72],
    'windSpeedKmh': [6, 22, 17, 5, 4, 6, 10, 11, 20, 4, 21, 10, 21, 17],
    'tempC': [22, 23, 34, 23, 22, 25, 24, 31, 30, 33, 24, 24, 25, 28]
}

df = pd.DataFrame(data)

X = df[['humPercent', 'windSpeedKmh']].values
y = df['tempC'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
newData = np.array([[90, 17]])
tempPredicition = model.predict(newData)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"Pred: {tempPredicition[0]:.2f}")
print(f"R2: {r2:.2f}")
print(f"MAE: {mae:.2f}")

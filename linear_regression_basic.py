# Simple Linear Regression Example

from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])
print("Prediction for X=5:", prediction[0])

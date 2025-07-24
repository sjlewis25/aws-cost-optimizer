import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the training data
df = pd.read_csv('training_data.csv')

# Features and target
X = df[['day_number']]
y = df['total_cost']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'cost_model.pkl')

print("Model trained and saved to cost_model.pkl")

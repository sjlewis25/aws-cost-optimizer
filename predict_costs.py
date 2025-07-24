import pandas as pd
import joblib
from datetime import datetime, timedelta

# Load trained model
model = joblib.load('cost_model.pkl')

# Predict for the next 7 days
future_dates = [datetime(2025, 7, 22) + timedelta(days=i) for i in range(7)]
day_numbers = [(date - datetime(2025, 6, 22)).days for date in future_dates]  # same base as training

# Create DataFrame
X_future = pd.DataFrame({'day_number': day_numbers})

# Predict future costs
predictions = model.predict(X_future)

# Show predictions
print("Predicted AWS Costs for Next 7 Days:")
for date, cost in zip(future_dates, predictions):
    print(f"{date.strftime('%Y-%m-%d')}: ${cost:.2f}")

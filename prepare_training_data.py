import pandas as pd

# Load the simulated cost data
df = pd.read_csv('simulated_costs.csv')

# Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum the cost
daily_costs = df.groupby('date').agg(total_cost=('cost', 'sum')).reset_index()

# Create a day_number column as a numeric index (for ML training)
daily_costs['day_number'] = (daily_costs['date'] - daily_costs['date'].min()).dt.days

# Save to CSV
daily_costs.to_csv('training_data.csv', index=False)

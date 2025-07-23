import pandas as pd

# Load the cost data
df = pd.read_csv('simulated_costs.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# 1. Total cost per service
service_costs = df.groupby('service')['cost'].sum().sort_values(ascending=False)

print("Total cost per service:")
print(service_costs)
print()

# 2. Top 3 most expensive services
top_services = service_costs.head(3)
print("Top 3 most expensive services:")
print(top_services)
print()

# 3. Daily total cost
daily_total = df.groupby('date')['cost'].sum()

# 4. Flagging days where cost exceeded threshold
threshold = 100
spike_days = daily_total[daily_total > threshold]

print(f"Days where total cost exceeded ${threshold}:")
print(spike_days)

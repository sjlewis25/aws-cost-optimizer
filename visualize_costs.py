import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('simulated_costs.csv')

df['date'] = pd.to_datetime(df['date'])

# Group total cost by date
daily_costs = df.groupby('date')['cost'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(daily_costs['date'], daily_costs['cost'], marker='o', linestyle='-')
plt.title('Simulated AWS Daily Cost')
plt.xlabel('Date')
plt.ylabel('Cost (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()


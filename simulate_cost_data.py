import pandas as pd
import random
from datetime import datetime, timedelta

services = ['EC2', 'S3', 'Lambda', 'RDS', 'CloudWatch', 'DynamoDB']
data = []

start_date = datetime.now() - timedelta(days=30)

for i in range(30):
    day = start_date + timedelta(days=i)
    for service in services:
        cost = round(random.uniform(0.5, 50), 2)
        data.append({
            'date': day.strftime('%Y-%m-%d'),
            'service': service,
            'cost': cost
        })

df = pd.DataFrame(data)
df.to_csv('simulated_costs.csv', index=False)
print("Simulated cost data saved to simulated_costs.csv")

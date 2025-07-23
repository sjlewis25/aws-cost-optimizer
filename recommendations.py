import pandas as pd

# Load the simulated cost data
df = pd.read_csv('simulated_costs.csv')

# Calculate average daily cost per service
average_costs = df.groupby('service')['cost'].mean()

# Define some basic recommendations
recommendations = []

for service, avg_cost in average_costs.items():
    if service == 'EC2' and avg_cost > 25:
        recommendations.append(f"EC2 average daily cost is ${avg_cost:.2f}. Consider rightsizing instances or switching to Spot Instances.")
    if service == 'S3' and avg_cost > 20:
        recommendations.append(f"S3 average daily cost is ${avg_cost:.2f}. Review storage classes and enable lifecycle policies.")
    if service == 'Lambda' and avg_cost > 15:
        recommendations.append(f"Lambda costs are high at ${avg_cost:.2f}/day. Check function memory allocations and invocation frequency.")
    if service == 'RDS' and avg_cost > 20:
        recommendations.append(f"RDS costs average ${avg_cost:.2f}/day. Consider turning on storage auto-scaling or switching to Aurora Serverless.")
    if service == 'CloudWatch' and avg_cost > 15:
        recommendations.append(f"CloudWatch costs are high at ${avg_cost:.2f}. Evaluate retention policies and log volume.")
    if service == 'DynamoDB' and avg_cost > 20:
        recommendations.append(f"DynamoDB average cost is ${avg_cost:.2f}/day. Consider using On-Demand mode or setting read/write auto-scaling.")

# Print recommendations
if recommendations:
    print("Cost Optimization Recommendations:\n")
    for r in recommendations:
        print(f"- {r}")
else:
    print("No high-cost services detected that require optimization.")

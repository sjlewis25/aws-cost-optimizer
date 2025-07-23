import pandas as pd

df = pd.read_csv("simulated_costs.csv")
df["date"] = pd.to_datetime(df["date"])

# Group by date to get daily total costs
daily_costs = df.groupby("date")["cost"].sum().reset_index()
daily_costs.columns = ["date", "total_cost"]

# Save to CSV for ML
daily_costs.to_csv("training_data.csv", index=False)
print("Saved training_data.csv")

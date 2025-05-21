import pandas as pd

# Load data (example)
df = pd.read_csv("data.csv")

# View first 3 rows
print(df.head(3))  # [1]

# Summary stats for numeric columns
print(df.describe())  # [1]

# Get specific column safely
ages = df.get("2024-25 2", pd.Series())  # [2]
print(ages)  # [2]
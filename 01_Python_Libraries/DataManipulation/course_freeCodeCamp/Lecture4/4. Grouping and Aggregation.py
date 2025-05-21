# GroupBy:
import pandas as pd

# Load data (example)
df = pd.read_csv("data2.csv")
print(df)  # [1]

grouped = df.groupby("department")["salary"].mean()
print(grouped)  # [2]
print(grouped["HR"])  # [2]
# Example 2: Group by department and apply multiple aggregations
agg_df = df.groupby("department").agg({
    "salary": ["mean", "max"],
    "age": "median"
})
print(agg_df)  # [3]
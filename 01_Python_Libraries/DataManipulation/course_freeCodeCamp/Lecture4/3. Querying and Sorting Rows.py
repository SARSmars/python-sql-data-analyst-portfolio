# Filtering Rows:
import pandas as pd

# Load data (example)
df = pd.read_csv("data.csv")

# Filter rows where age > 30
filtered_df1 = df[df["2024-25 2"] > 7]
print(filtered_df1)  # [1]

# Filter rows where age > 30
filtered_df2 = df[df["2024-25 2"] < 6]
print(filtered_df2)  # [1]

# Combine conditions
filtered_df3 = df[(df["2024-25 2"] > 6) & (df["2024-25 2"] < 6.3)]  
print(filtered_df3)  # [2]

# Sorting
sorted_df = df.sort_values(by="2024-25 2", ascending=True)  # [3]
print(sorted_df)  # [3]
# Sorting by multiple columns
sorted_df_multi = df.sort_values(by=["2024-25 2", "2024-25 1"], ascending=[True, False])  # [4]
print(sorted_df_multi)  # [4]
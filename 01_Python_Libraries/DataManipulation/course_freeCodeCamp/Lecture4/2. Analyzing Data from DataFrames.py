import pandas as pd


# Load data (example)
df = pd.read_csv("data.csv")

print(df.mean())   # Mean of numeric columns [1]
print(df.mode())   # Most frequent values [1]
print(df.median()) # Median values [1]

# Creating New Columns:

df["2024-2025"] = df["2024-25 1"] /2 + df["2024-25 2"] /2
print(df["2024-2025"])  # [2]
print(df["2024-2025"].mean())  # Mean of new column [2]
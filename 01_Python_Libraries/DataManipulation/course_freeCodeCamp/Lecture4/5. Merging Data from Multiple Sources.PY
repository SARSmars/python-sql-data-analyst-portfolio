# Joins:

import pandas as pd
# Inner join on 'employee_id'
# Load data (example)
df1 = pd.DataFrame({
    "employee_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})
df2 = pd.DataFrame({
    "employee_id": [2, 3, 4],
    "salary": [70000, 80000, 90000]
})
merged_df = pd.merge(df1, df2, on="employee_id", how="inner")  
print(merged_df)  # [1]

# Concatenate vertically
combined_df = pd.concat([df1, df2], axis=0)  
print(combined_df)  # [2]

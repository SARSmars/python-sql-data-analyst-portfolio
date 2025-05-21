

import pandas as pd
import numpy as np

# Load sample data
df = pd.read_csv('eda_sample_data.csv')

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Remove duplicates
df = df.drop_duplicates()

# Correct data types
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

# Handle outliers (cap Salary at 3 std deviations)
salary_cap = df['Salary'].mean() + 3 * df['Salary'].std()
df['Salary'] = np.where(df['Salary'] > salary_cap, salary_cap, df['Salary'])

# ✅ Save the cleaned data to a new CSV file
df.to_csv('eda_cleaned_data.csv', index=False)

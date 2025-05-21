import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

from statsmodels.tsa.api import ExponentialSmoothing, Holt, SimpleExpSmoothing
from sklearn.linear_model import LinearRegression

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('gold_monthly_csv.csv')
print(df.head())
print(df.tail())

# Print the range of the gold price available

print(f"The range of the gold price available is from {df['Date'].min()} to {df['Date'].max()}")

date = pd.date_range (start= '2000-01-01', end= '2023-01-01', freq='M')
print(date)
print(len(df))
print(len(date))

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
print(df.head())

# Plot Graph

df.plot(figsize=(20,8))
plt.title("Gold price monthly since 1950")
plt.xlabel("month")
plt.ylabel("price")
plt.grid() 
plt.show()

# Descrite the data

print(df.describe())
print(round(df.describe(), 3))
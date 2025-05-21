# Visualization:
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")
# Basic statistics
print(df.describe())  # Summary statistics
# Line plot for time series
df.plot.line(x="date", y="sales", title="Sales Over Time")  

plt.savefig("sales_trend.png")  # Save the line plot
plt.show()

# Bar plot
df["department"].value_counts().plot.bar(title="Department Distribution")  

# Save plot
plt.savefig("sales_trend.png")  
plt.show()
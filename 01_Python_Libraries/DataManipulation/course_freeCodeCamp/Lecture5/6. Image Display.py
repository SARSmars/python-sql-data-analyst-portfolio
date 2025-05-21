
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Create a time series DataFrame
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=30)
value = np.cumsum(np.random.randn(30)) + 50  # Trend-like data

# Create scatter data
x_vals = np.random.rand(30) * 100
y_vals = x_vals * 0.5 + np.random.randn(30) * 10

# Product sales
products = ['A', 'B', 'C', 'D']
product_data = np.random.choice(products, size=30)
sales = np.random.randint(100, 500, size=30)

# Final DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Value': value,
    'X': x_vals,
    'Y': y_vals,
    'Product': product_data,
    'Sales': sales
})

# Save to CSV
df.to_csv('multi_plot_data.csv', index=False)

# Correlation matrix
corr = df[['Value', 'X', 'Y', 'Sales']].corr()
corr.to_csv('correlation_matrix.csv')

# Purpose: Visualize matrix-like data (e.g., correlations).
# Generate sample image data
image_data = np.random.rand(10,10)

plt.imshow(image_data, cmap='viridis')
plt.colorbar()
plt.title('Matrix Visualization')

fig, ax = plt.subplots(2,2, figsize=(10,8))

# Plot 1
sns.lineplot(x='Date', y='Value', data=df, ax=ax[0,0])

# Plot 2
sns.scatterplot(x='X', y='Y', data=df, ax=ax[0,1])

# Plot 3
sns.barplot(x='Product', y='Sales', data=df, ax=ax[1,0])

# Plot 4
sns.heatmap(corr, ax=ax[1,1])

plt.tight_layout()
plt.savefig('image_display.png')
plt.show()
plt.close()
# Save the plot
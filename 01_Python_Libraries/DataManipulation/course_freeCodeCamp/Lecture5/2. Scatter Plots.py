import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Generate random data
# for scatter plot
# Create a DataFrame with random data

data = {'X': np.random.randn(100),
        'Y': np.random.randn(100)*2 + 5,
        'Category': np.random.choice(['A','B'], 100)}
pd.DataFrame(data).to_csv('scatter_data.csv', index=False)


df = pd.read_csv('scatter_data.csv')

# Basic scatter
plt.scatter(df['X'], df['Y'])
plt.title('Basic Scatter Plot')

# Advanced with Seaborn
sns.scatterplot(x='X', y='Y', hue='Category', 
                style='Category', data=df, s=100)
plt.title('Multivariate Scatter Plot')
plt.savefig('scatter_plot.png')
plt.show()
# Save the plot
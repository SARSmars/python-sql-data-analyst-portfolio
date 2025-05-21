
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate random data
# for histogram
# Create a DataFrame with random data

pd.DataFrame({'Scores': np.concatenate([
    np.random.normal(70, 10, 500),
    np.random.normal(90, 5, 500)
])}).to_csv('distribution_data.csv', index=False)

df = pd.read_csv('distribution_data.csv')

# Matplotlib histogram
plt.hist(df['Scores'], bins=30, edgecolor='k')
plt.title('Score Distribution')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.show()
plt.close()
# Save the plot
# Advanced with Seaborn
sns.histplot(df['Scores'], bins=30, kde=False)
# Seaborn KDE plot
sns.histplot(df['Scores'], kde=True, bins=30)
plt.title('Density Estimate')
plt.title('Seaborn Histogram')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.savefig('seaborn_histogram.png')
plt.show()
plt.close()
# Save the plot

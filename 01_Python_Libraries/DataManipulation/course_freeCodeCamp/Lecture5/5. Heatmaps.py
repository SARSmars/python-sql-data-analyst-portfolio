
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Purpose: Visualize matrix-like data (e.g., correlations).

corr = pd.DataFrame(np.random.randn(10,10)).corr()
corr.to_csv('correlation_matrix.csv')

corr = pd.read_csv('correlation_matrix.csv', index_col=0)



plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', 
           vmin=-1, vmax=1, linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.show()
plt.close()
# Save the plot
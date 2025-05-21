
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'Product': ['A', 'B', 'C', 'D'],
        'Sales': [45, 78, 32, 65]}
pd.DataFrame(data).to_csv('sales_data.csv', index=False)
df = pd.read_csv('sales_data.csv')

df = pd.read_csv('sales_data.csv')

# Vertical bar chart
sns.barplot(x='Product', y='Sales', data=df)
plt.title('Product Sales Comparison')
plt.savefig('bar_chart.png')
plt.show()
plt.close()

# Horizontal bar chart
plt.barh(df['Product'], df['Sales'])
plt.title('Horizontal Bar Chart')
plt.xlabel('Sales')
plt.ylabel('Product')
plt.savefig('horizontal_bar_chart.png')
plt.show()
plt.close()
# Save the plot

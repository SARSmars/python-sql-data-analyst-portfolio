import pandas as pd
data = {'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
        'Value': [i*0.5 + i**1.2 for i in range(30)]}
df = pd.DataFrame(data)
df.to_csv('trend_data.csv', index=False)

import matplotlib.pyplot as plt
import seaborn as sns

# Basic line plot
plt.plot(df['Date'], df['Value'])
plt.title('Time Series Trend')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Seaborn-styled line plot
sns.set_style("whitegrid")
plt.figure(figsize=(10,4))
sns.lineplot(x='Date', y='Value', data=df, marker='o')
plt.title('Enhanced Time Series (Seaborn)')
plt.tight_layout()




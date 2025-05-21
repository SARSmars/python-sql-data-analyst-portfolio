import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load sample data
df = pd.read_csv('eda_sample_data.csv')

# Clean missing values
df.dropna(subset=['Age', 'Salary', 'Department'], inplace=True)

# Summary statistics
summary_stats = df.describe()
summary_stats.to_csv('eda_summary_stats.csv')

# Distribution: Age
plt.figure(figsize=(10,4))
sns.histplot(df['Age'], bins=15, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age_distribution.png')
plt.close()

# Boxplot: Salary by Department
plt.figure(figsize=(10,4))
sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Salary Distribution by Department')
plt.savefig('salary_boxplot.png')
plt.close()

# Scatter: Age vs Salary by Department
plt.figure(figsize=(8,6))
sns.scatterplot(x='Age', y='Salary', hue='Department', data=df)
plt.title('Age vs Salary by Department')
plt.savefig('age_salary_scatter.png')
plt.close()

# Grouping and aggregation
dept_salary_mean = df.groupby('Department')['Salary'].mean()
dept_salary_mean.to_csv('eda_dept_salary_mean.csv')

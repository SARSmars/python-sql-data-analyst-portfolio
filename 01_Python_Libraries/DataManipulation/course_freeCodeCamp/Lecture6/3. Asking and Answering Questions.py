from scipy.stats import f_oneway
import pandas as pd

df = pd.read_csv('eda_sample_data.csv')

# ANOVA: Does department affect salary?
anova_result = f_oneway(
    df[df['Department'] == 'HR']['Salary'],
    df[df['Department'] == 'Tech']['Salary'],
    df[df['Department'] == 'Sales']['Salary'],
    df[df['Department'] == 'Finance']['Salary']
)

print("ANOVA p-value:", anova_result)

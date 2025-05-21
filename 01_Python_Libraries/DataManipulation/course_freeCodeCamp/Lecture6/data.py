import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Heidi',
             'Ivan', 'Judy', 'Kevin', 'Laura', 'Mike', 'Nancy', 'Eva'],
    'Age': [25, 30, np.nan, 45, 29, 31, 28, 34, 38, np.nan, 40, 36, 33, 29, 29],
    'Salary': [50000, 52000, 48000, 51000, 53000, np.nan, 60000, 150000,
               52000, 51000, 200000, 48000, 49000, 51000, 53000],
    'JoiningDate': ['2022-01-15', '2022-02-10', '2021-12-01', '2022-03-20',
                    '2022-04-11', '2022-05-25', '2021-11-05', '2022-06-30',
                    '2022-01-15', '2022-03-20', '2022-07-18', '2022-08-03',
                    '2022-09-10', '2022-04-11', '2022-04-11']
}

df = pd.DataFrame(data)
df.to_csv('eda_sample_data.csv', index=False)

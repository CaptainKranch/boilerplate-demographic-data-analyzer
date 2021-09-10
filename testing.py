import pandas as pd

df = pd.read_csv('adult.data.csv')

average_age_men = df[df['sex'] == 'Male']['age'].mean()
print(average_age_men)

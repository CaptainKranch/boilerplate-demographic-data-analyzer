import pandas as pd

df = pd.read_csv('adult.data.csv')
#
# race_count = df['race'].value_counts()
#
# average_age_men = df[df['sex'] == 'Male'].mean()

percentage_bachelors = df[df['education'] == 'Bachelors'].value_counts()
percentage_bachelors = ((percentage_bachelors/len(df)) * 100)
print(percentage_bachelors)

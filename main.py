import pandas as pd

PATH_1 = 'data/winequality-red.csv'
PATH_2 = 'data/winequality-white.csv'

df1 = pd.read_csv(PATH_1)
df2 = pd.read_csv(PATH_2)

print(df1.head(10))
print(df2.head(10))
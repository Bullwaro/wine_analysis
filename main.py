import pandas as pd
from prettytable import PrettyTable

from table_output import print_table, print_selected_columns
from constants import TABLE_1_NAME, TABLE_2_NAME, PATH_1, PATH_2

df1 = pd.read_csv(PATH_1, sep=';')
df2 = pd.read_csv(PATH_2, sep=';')

print(TABLE_1_NAME)
print(df1.head())
print("Table shape:", df1.shape, sep='\n')
print("Table info:")
df1.info()
print("Total missing values:", df1.isna().sum().sum())

print(TABLE_2_NAME)
print(df2.head())
print("Table shape:", df2.shape, sep='\n')
print("Table info:")
df2.info()
print("Total missing values:", df2.isna().sum().sum())
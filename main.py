import pandas as pd
from prettytable import PrettyTable

from table_output import print_selected_columns

PATH_1 = 'data/winequality-red.csv'
PATH_2 = 'data/winequality-white.csv'

df1 = pd.read_csv(PATH_1, sep=';')
df2 = pd.read_csv(PATH_2, sep=';')



#print(df2.head().values.tolist())
print_selected_columns(df1, ['residual sugar', 'density'])
#print_table(df1.columns, df1.head(10).values.tolist())
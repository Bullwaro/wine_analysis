import pandas as pd
from prettytable import PrettyTable

from table_output import print_table, print_selected_columns
from constants import TABLE_1_NAME, TABLE_2_NAME, PATH_1, PATH_2
from user_menu import main_menu

df1 = pd.read_csv(PATH_1, sep=';')
df2 = pd.read_csv(PATH_2, sep=';')
cur = None
db_list = {
    TABLE_1_NAME : {
        'obj' : df1,
        'sep' : ';'
        }, 
    TABLE_2_NAME : {
        'obj' : df2,
        'sep' : ';'
        }
    }

main_menu(cur, db_list)
'''
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
'''
#print(df1.describe())
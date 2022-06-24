import pandas as pd

temp = pd.read_csv("temp.csv", parse_dates=['datetime'], index_col='datetime')

# print(temp.head())

# print(temp.info())

print(temp.iloc[0,0])

# print(type(temp.iloc[0,0]))

#قسمت ۱ از پارت ۹ تموم شد
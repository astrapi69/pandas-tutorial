import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
#
# print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#
# print(df)
#
# print(df.head())
#
# print(df.tail(3))

print(df.index)
print("##################")

print(df.columns)

df['E'] = ['one','one', 'two','three','four','three']

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102',periods=6))

print("##################")

print(s1)
print("##################")

df['F'] = s1
print(df)

print("##################")
df.at[dates[0],'A'] = 0
print(df)






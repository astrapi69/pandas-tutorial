import pandas as pd

df = pd.DataFrame([
  ["Amy","Assignment 1",75],
  ["Amy","Assignment 2",35],
  ["Bob","Assignment 1",99],
  ["Bob","Assignment 2",35]
  ], columns=["Name", "Assignment", "Grade"])

prdf.groupby('Name').Grade.mean()

print(df)
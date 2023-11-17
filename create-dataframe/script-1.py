import pandas as pd


df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt','skirt' ],
  'Color': ['blue', 'green', 'red','black' ],
  # add Product Name and Color here
})

print(df1)

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3],
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})

print(df1)
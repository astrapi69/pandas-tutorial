import pandas as pd


# Import the wardrobe.csv data: wardrobe
wardrobe = pd.read_csv('wardrobe.csv')

print(wardrobe)
wardrobe['Product'] = "default Product"
wardrobe['Name'] = "default name"
print(wardrobe)

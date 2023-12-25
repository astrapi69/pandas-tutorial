import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4))

print("######### df #########")
print(df)
print("##################")

pieces = [df[:3]]

print("######## pieces ##########")
print(pieces)
print("##################")
pieces = [df[3:7]]

print("######## pieces ##########")
print(pieces)
print("##################")
pieces = [df[7:]]

print("######## pieces ##########")
print(pieces)
print("##################")
print("##################")

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
print("######## pieces ##########")
print(pieces)
print("##################")
print("##################")
print("##################")
print("##################")
print("##################")
print("##################")
print(pd.concat(pieces))
print("##################")
print("##################")
print("##################")
print("##################")
print("##################")
print("##################")





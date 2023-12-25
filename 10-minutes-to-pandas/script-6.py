import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4))

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})


print("######## left ##########")
print(left)
print("##################")

print("######## right ##########")
print(right)
print("##################")

mergedDf = pd.merge(left, right, on='key')

print("######## mergedDf ##########")
print(mergedDf)
print("##################")
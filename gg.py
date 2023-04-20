import numpy as np
import pandas as pd

columns = ['Sepal ka length', 'Sepal ka width', 'Petal ka length', 'Petal ka width', 'Class_labels']

df = pd.read_csv('iris.data', names=columns)
df.head()

print(df[10:21])

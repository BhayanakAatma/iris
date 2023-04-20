import numpy as np
import pandas as pd

columns = ['SepalLengthCm', 'Sepal ka width', 'Petal ka length', 'Petal ka width', 'Class_labels']

df = pd.read_csv('iris.data', names=columns)
df.head()

sum_data = df["SepalLengthCm"].sum()
mean_data = df["SepalLengthCm"].mean()
median_data = df["SepalLengthCm"].median()

print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)


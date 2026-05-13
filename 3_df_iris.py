import pandas as pd
import numpy as np
     

data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Priya', 'Karan', 'Sneha'],
    'Department': ['IT', 'HR', 'IT', 'Finance',
                   'HR', 'Finance'],
    'Age': [21, 22, 20, 23, 21, 22],
    'Income': [25000, 30000, 22000, 35000, 28000, 32000]
}

df = pd.DataFrame(data)

print(df)
     

grouped = df.groupby('Department')['Income']

print("Mean")
print(grouped.mean())

print("\nMedian")
print(grouped.median())

print("\nMinimum")
print(grouped.min())

print("\nMaximum")
print(grouped.max())

print("\nStandard Deviation")
print(grouped.std())
     

income_list = df.groupby('Department')['Income'].apply(list)

print(income_list)

df = pd.read_csv("datasets/iris.csv")

print(df.head())
     

print(df.groupby('species').describe())
     

print(df.groupby('species').mean())
     

print(df.groupby('species').std())
     

print(df.groupby('species').quantile([0.25, 0.5, 0.75]))
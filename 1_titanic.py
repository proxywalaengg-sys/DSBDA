import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Statistical summary
print(df.describe())

# Dataset information
print(df.info())

# Shape of dataset
print("Shape of Dataset:", df.shape)

# Display data types
print(df.dtypes)

# Fill missing Age values and convert to integer
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Age'] = df['Age'].astype(int)

print(df['Age'].dtypes)

# Normalize Fare column
df['Fare'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

print(df['Fare'].head())

# Convert categorical variable Sex into numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print(df['Sex'].head())
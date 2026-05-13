import pandas as pd
import numpy as np

# Create dataset
data = {
    'Name': ['Amit', 'Neha', 'Ravi', 'Priya', 'Karan', 'Sneha', 'Raj'],
    'Maths': [85, 90, np.nan, 95, 40, 500, 78],
    'Science': [88, 92, 85, np.nan, 35, 96, 80],
    'English': [75, 85, 80, 70, 30, 90, np.nan],
    'Attendance': [90, 95, 85, 80, 75, 110, 88]
}

df = pd.DataFrame(data)

print(df)

# 1. Scan for Missing Values and Inconsistencies

print(df.isnull().sum())

# Fill missing values using mean
df['Maths'] = df['Maths'].fillna(df['Maths'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['English'] = df['English'].fillna(df['English'].mean())

print(df)

# Find attendance values greater than 100
print(df[df['Attendance'] > 100])

# Replace attendance >100 with 100
df.loc[df['Attendance'] > 100, 'Attendance'] = 100

print(df)

# 2. Detect and Handle Outliers

Q1 = df['Maths'].quantile(0.25)
Q3 = df['Maths'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Detect outliers
outliers = df[(df['Maths'] < lower_limit) | (df['Maths'] > upper_limit)]

print(outliers)

# Remove outliers
df = df[(df['Maths'] >= lower_limit) & (df['Maths'] <= upper_limit)]

print(df)

# 3. Apply Data Transformation

# Normalize Attendance column
df['Attendance'] = (
    (df['Attendance'] - df['Attendance'].min()) /
    (df['Attendance'].max() - df['Attendance'].min())
)

print(df['Attendance'])
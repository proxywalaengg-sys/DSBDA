import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Boxplot
sns.boxplot(
    x='sex',
    y='age',
    hue='survived',
    data=df
)

plt.title("Age Distribution with Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")

plt.show()
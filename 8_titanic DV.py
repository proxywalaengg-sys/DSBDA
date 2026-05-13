import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# ----------------------------------
# 1. Finding Patterns in Dataset
# ----------------------------------

# Count plot for survival
sns.countplot(x='survived', data=df)

plt.title("Survival Count")
plt.show()

# Survival based on gender
sns.countplot(x='sex', hue='survived', data=df)

plt.title("Survival Based on Gender")
plt.show()

# Passenger class distribution
sns.countplot(x='class', data=df)

plt.title("Passenger Class Distribution")
plt.show()

# ----------------------------------
# 2. Histogram of Fare
# ----------------------------------

plt.hist(df['fare'], bins=30)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.show()
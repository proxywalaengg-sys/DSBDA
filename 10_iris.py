import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
df = sns.load_dataset('iris')

# Display first 5 rows
print(df.head())

# -----------------------------------
# 1. Features and Their Types
# -----------------------------------

print("\nFeatures and Data Types:\n")
print(df.dtypes)

# -----------------------------------
# 2. Histograms for Each Feature
# -----------------------------------

df.hist(figsize=(10, 8))

plt.suptitle("Histogram of Iris Features")
plt.show()

# -----------------------------------
# 3. Boxplots for Each Feature
# -----------------------------------

features = df.columns[:-1]

for feature in features:

    plt.figure(figsize=(6, 4))

    sns.boxplot(y=df[feature])

    plt.title(f"Boxplot of {feature}")

    plt.show()

# -----------------------------------
# 4. Compare Distributions
# -----------------------------------

print("\nStatistical Summary:\n")
print(df.describe())
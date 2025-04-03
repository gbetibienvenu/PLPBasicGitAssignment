# This is week 7 tasks done and dusted
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
# Map target numbers to species names
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display first few rows
print("First few rows of the dataset:")
print(df.head())

# Check data types and missing values
df.info()

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean for numerical columns
grouped_means = df.groupby('species').mean()
print("\nAverage values per species:")
print(grouped_means)

# Task 3: Data Visualization
sns.set_style("whitegrid")

# 1. Line Chart - Petal Length over Index
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length", color="blue")
plt.title("Petal Length Trend Over Index")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - Average Sepal Length per Species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="sepal length (cm)", data=df, palette="viridis")
plt.title("Average Sepal Length per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 3. Histogram - Distribution of Petal Width
plt.figure(figsize=(8, 5))
sns.histplot(df["petal width (cm)"], bins=15, kde=True, color="green")
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Count")
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="coolwarm")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

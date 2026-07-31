import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
file_name = input("Enter CSV file name: ")
df = pd.read_csv(file_name)

# Theme
sns.set_theme(style="whitegrid")

# Numeric Columns
num_cols = df.select_dtypes(include="number").columns

# 1. Histplot
plt.figure(figsize=(6,4))
sns.histplot(df[num_cols[0]], kde=True)
plt.title("Histogram")
plt.savefig("1_histogram.png")
plt.show()
print("Insight: Shows the distribution of the first numeric feature.\n")

# 2. KDE Plot
plt.figure(figsize=(6,4))
sns.kdeplot(df[num_cols[0]], fill=True)
plt.title("KDE Plot")
plt.savefig("2_kde.png")
plt.show()
print("Insight: Displays the density distribution of the data.\n")

# 3. Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(y=df[num_cols[0]])
plt.title("Box Plot")
plt.savefig("3_boxplot.png")
plt.show()
print("Insight: Detects outliers in the dataset.\n")

# 4. Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(y=df[num_cols[0]])
plt.title("Violin Plot")
plt.savefig("4_violin.png")
plt.show()
print("Insight: Shows distribution and density together.\n")

# 5. Count Plot (First Categorical Column)
cat_cols = df.select_dtypes(include="object").columns

if len(cat_cols) > 0:
    plt.figure(figsize=(6,4))
    sns.countplot(x=df[cat_cols[0]])
    plt.xticks(rotation=45)
    plt.title("Count Plot")
    plt.savefig("5_countplot.png")
    plt.show()
    print("Insight: Shows category frequency.\n")

# 6. Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("6_heatmap.png")
plt.show()
print("Insight: Shows correlation between numeric features.\n")

# 7. Pair Plot
sns.pairplot(df[num_cols])
plt.savefig("7_pairplot.png")
plt.show()
print("Insight: Displays pairwise relationships.\n")

# 8. Correlation Matrix
print("\nCorrelation Matrix:")
print(df[num_cols].corr())

# 9. Scatter Plot
if len(num_cols) >= 2:
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=df[num_cols[0]], y=df[num_cols[1]])
    plt.title("Scatter Plot")
    plt.savefig("8_scatter.png")
    plt.show()
    print("Insight: Shows relationship between two variables.\n")

# 10. Bar Plot
if len(cat_cols) > 0 and len(num_cols) > 0:
    plt.figure(figsize=(8,4))
    sns.barplot(x=cat_cols[0], y=num_cols[0], data=df)
    plt.xticks(rotation=45)
    plt.title("Bar Plot")
    plt.savefig("9_barplot.png")
    plt.show()
    print("Insight: Compares average values across categories.\n")

print("EDA Visual Report Generated Successfully!")
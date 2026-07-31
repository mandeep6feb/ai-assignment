import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
file_name = input("Enter CSV file name: ")
df = pd.read_csv(file_name)

# Select Numeric Columns
numeric_cols = df.select_dtypes(include='number').columns

if len(numeric_cols) < 2:
    print("Dataset must contain at least 2 numeric columns.")
    exit()

x = numeric_cols[0]
y = numeric_cols[1]

# Create Dashboard
plt.figure(figsize=(12,8))

# 1. Line Plot
plt.subplot(2,2,1)
plt.plot(df[x], df[y], marker='o')
plt.title("Line Plot")
plt.xlabel(x)
plt.ylabel(y)

# 2. Bar Plot
plt.subplot(2,2,2)
plt.bar(df[x], df[y])
plt.title("Bar Plot")
plt.xlabel(x)
plt.ylabel(y)

# 3. Scatter Plot
plt.subplot(2,2,3)
plt.scatter(df[x], df[y])
plt.title("Scatter Plot")
plt.xlabel(x)
plt.ylabel(y)

# 4. Histogram
plt.subplot(2,2,4)
plt.hist(df[y], bins=10)
plt.title("Histogram")
plt.xlabel(y)
plt.ylabel("Frequency")

# Adjust Layout
plt.tight_layout()

# Save Dashboard
plt.savefig("visualization_dashboard.png")

# Show Dashboard
plt.show()

print("\nDashboard created successfully!")
print("Saved as: visualization_dashboard.png")
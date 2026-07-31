import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load CSV
file_name = input("Enter CSV file name (e.g. student.csv): ")
df = pd.read_csv(file_name)

print("\nOriginal Shape:", df.shape)

summary = []

# Missing Values
missing_before = df.isnull().sum().sum()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

missing_after = df.isnull().sum().sum()

summary.append(["Missing Values", missing_before, missing_after])

# Remove Duplicates
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()
duplicates_after = df.duplicated().sum()

summary.append(["Duplicates", duplicates_before, duplicates_after])

# String Cleaning
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().str.title()

summary.append(["String Cleaning", "Done", "Done"])

# Data Type Conversion
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass

summary.append(["Data Type Conversion", "Checked", "Completed"])

# Outlier Removal (IQR)
numeric_cols = df.select_dtypes(include=np.number).columns

rows_before = len(df)

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

rows_after = len(df)

summary.append(["Outliers Removed", rows_before - rows_after, "Removed"])

# Feature Scaling
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

summary.append(["Normalization", "Done", "Done"])

# Save Cleaned CSV
df.to_csv("cleaned_data.csv", index=False)

# Summary Report
report = pd.DataFrame(summary,
                      columns=["Process", "Before", "After"])

print("\nCleaning Summary")
print(report)

report.to_csv("cleaning_summary_report.csv", index=False)

print("\nCleaned CSV Saved : cleaned_data.csv")
print("Summary Report Saved : cleaning_summary_report.csv")
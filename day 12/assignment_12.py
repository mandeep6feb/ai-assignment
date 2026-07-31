import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Load Dataset
file_name = input("Enter CSV file name: ")
df = pd.read_csv(file_name)

print("\n===== Statistical Summary Report =====\n")

# Numeric Columns
numeric_cols = df.select_dtypes(include=np.number).columns

# Descriptive Statistics
summary = pd.DataFrame({
    "Mean": df[numeric_cols].mean(),
    "Median": df[numeric_cols].median(),
    "Mode": df[numeric_cols].mode().iloc[0],
    "Variance": df[numeric_cols].var(),
    "Std_Deviation": df[numeric_cols].std()
})

print("Descriptive Statistics")
print(summary)

# Correlation Matrix
print("\nCorrelation Matrix")
print(df[numeric_cols].corr())

# Random Sampling (20%)
sample = df.sample(frac=0.2, random_state=42)

print("\nSample Size:", len(sample))

# Hypothesis Test (Independent t-test)
if len(numeric_cols) >= 2:

    col1 = df[numeric_cols[0]]
    col2 = df[numeric_cols[1]]

    t_stat, p_value = ttest_ind(col1, col2)

    print("\nHypothesis Test (t-test)")
    print("T-Statistic :", t_stat)
    print("P-Value :", p_value)

    if p_value < 0.05:
        print("Result: Reject Null Hypothesis")
    else:
        print("Result: Fail to Reject Null Hypothesis")

# Save Reports
summary.to_csv("statistical_summary_report.csv")

df[numeric_cols].corr().to_csv("correlation_matrix.csv")

print("\nReports Saved Successfully!")
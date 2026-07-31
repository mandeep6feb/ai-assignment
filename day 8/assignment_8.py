import pandas as pd

# Load CSV Files
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")

# Merge Sales and Customers
data = pd.merge(sales, customers, on="CustomerID", how="inner")

# Merge with Products
data = pd.merge(data, products, on="ProductID", how="inner")

# Create Revenue Column
data["Revenue"] = data["Quantity"] * data["Price"]

# Department-wise Revenue Report
department_report = data.groupby("Department")["Revenue"].sum().reset_index()

print("\nDepartment-wise Revenue Report")
print(department_report)

# Pivot Table
pivot = pd.pivot_table(
    data,
    values="Revenue",
    index="Department",
    aggfunc="sum"
)

print("\nPivot Table")
print(pivot)

# Save Reports
department_report.to_csv("department_revenue_report.csv", index=False)
pivot.to_csv("pivot_report.csv")

print("\nReports Generated Successfully!")
import pandas as pd
data = {
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop"],
    "Customer": ["A", "B", "C", "D", "E", "F"],
    "Sales": [5, 10, 8, 6, 12, 7],
    "Revenue": [250000, 150000, 400000, 180000, 240000, 350000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 1. Monthly Sales
print("\nMonthly Sales:")
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

# 2. Best Performing Product
print("\nBest Performing Product:")
best_product = df.groupby("Product")["Sales"].sum()
print(best_product)
print("Best Product:", best_product.idxmax())

# 3. Highest Revenue
print("\nHighest Revenue Record:")
print(df.loc[df["Revenue"].idxmax()])

# 4. Customer Summary
print("\nCustomer Summary:")
customer_summary = df.groupby("Customer")[["Sales", "Revenue"]].sum()
print(customer_summary)

# 5. Sales Report
print("\nSales Report:")
print(df.describe())

### exporting
df.to_csv("sales_report.csv", index=False)

print("\nSales report exported successfully as sales_report.csv")
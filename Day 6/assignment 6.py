import pandas as pd

data = pd.read_csv("sales.csv")

data["Revenue"] = data["Quantity"] * data["Price"]

data["Month"] = pd.to_datetime(data["Date"]).dt.month
monthly_sales = data.groupby("Month")["Revenue"].sum()

print("Monthly Sales:")
print(monthly_sales)

product_sales = data.groupby("Product")["Revenue"].sum()
print("\nBest Performing Product:")
print(product_sales.idxmax())

print("\nHighest Revenue:")

customer = data.groupby("Customer")["Revenue"].sum()
print("\nCustomer Summary:")
print(customer)

data = data.sort_values("Revenue", ascending=False)

data.to_csv("sales_report.csv", index=False)

print("\nSales Report Created!")
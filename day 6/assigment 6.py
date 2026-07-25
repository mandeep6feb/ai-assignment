import pandas as pd
df = pd.read_csv("sales_data.csv")
print("Original Data")
print(df)
df = df.dropna()
print("\nAfter Cleaning")
print(df)
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(
    df["Date"].dt.month
)["Sales"].sum()
print("\nMonthly Sales")
print(monthly_sales)
product_sales = df.groupby(
    "Product"
)["Sales"].sum()
best_product = product_sales.idxmax()
print("\nBest Product:")
print(best_product)
highest_revenue = df["Revenue"].max()
print("\nHighest Revenue:")
print(highest_revenue)
customer_summary = df.groupby(
    "Customer"
).agg(
    Total_Sales=("Sales","sum"),
    Total_Revenue=("Revenue","sum")
)
print("\nCustomer Summary")
print(customer_summary)
top_performers = df.sort_values(
    by="Sales",
    ascending=False
)
print("\nTop Performers")
print(top_performers)
summary = df.groupby(
    "Product"
).agg(
    Total_Sales=("Sales","sum"),
    Average_Sales=("Sales","mean")
)
print(summary)
monthly_sales.to_csv("monthly_sales_report.csv")
customer_summary.to_csv(
    "customer_summary.csv"
)
top_performers.to_csv(
    "sales_report.csv",
    index=False
)
print("\nReports Exported Successfully")
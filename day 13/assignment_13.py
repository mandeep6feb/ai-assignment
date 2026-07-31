import sqlite3
import pandas as pd

# Create Database
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Customer Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
CustomerID INTEGER PRIMARY KEY,
CustomerName TEXT,
City TEXT
)
""")

# Product Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
ProductID INTEGER PRIMARY KEY,
ProductName TEXT,
Category TEXT,
Price REAL
)
""")

# Sales Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales(
SaleID INTEGER PRIMARY KEY,
CustomerID INTEGER,
ProductID INTEGER,
Quantity INTEGER,
FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
)
""")

# Insert Data
cursor.executemany("INSERT INTO Customers VALUES (?,?,?)",[
(1,'Rahul','Delhi'),
(2,'Priya','Mumbai'),
(3,'Amit','Jaipur')
])

cursor.executemany("INSERT INTO Products VALUES (?,?,?,?)",[
(101,'Laptop','Electronics',50000),
(102,'Shoes','Fashion',3000),
(103,'Chair','Furniture',4000)
])

cursor.executemany("INSERT INTO Sales VALUES (?,?,?,?)",[
(1,1,101,2),
(2,2,102,5),
(3,3,103,3),
(4,1,102,2),
(5,2,101,1)
])

conn.commit()

queries = {

"Q1":"SELECT * FROM Customers;",

"Q2":"SELECT * FROM Products WHERE Price>4000;",

"Q3":"SELECT Category,AVG(Price) AS AvgPrice FROM Products GROUP BY Category;",

"Q4":"SELECT * FROM Products ORDER BY Price DESC;",

"Q5":"""
SELECT CustomerName,ProductName,Quantity
FROM Sales
INNER JOIN Customers
ON Sales.CustomerID=Customers.CustomerID
INNER JOIN Products
ON Sales.ProductID=Products.ProductID;
""",

"Q6":"""
SELECT CustomerName,COUNT(SaleID) AS TotalOrders
FROM Customers
LEFT JOIN Sales
ON Customers.CustomerID=Sales.CustomerID
GROUP BY CustomerName;
""",

"Q7":"""
SELECT Category,SUM(Quantity*Price) AS Revenue
FROM Sales
JOIN Products
ON Sales.ProductID=Products.ProductID
GROUP BY Category;
""",

"Q8":"""
SELECT ProductName,Price
FROM Products
WHERE Price>(
SELECT AVG(Price) FROM Products
);
""",

"Q9":"""
SELECT CustomerName,SUM(Quantity*Price) AS TotalSpent
FROM Sales
JOIN Customers
ON Sales.CustomerID=Customers.CustomerID
JOIN Products
ON Sales.ProductID=Products.ProductID
GROUP BY CustomerName
ORDER BY TotalSpent DESC;
""",

"Q10":"""
SELECT ProductName,SUM(Quantity) AS TotalSold
FROM Sales
JOIN Products
ON Sales.ProductID=Products.ProductID
GROUP BY ProductName;
"""
}

for name,query in queries.items():
    print(f"\n{name}")
    print(pd.read_sql(query,conn))

conn.close()
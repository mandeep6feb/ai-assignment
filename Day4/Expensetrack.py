import json
import csv
import os

FILE = "expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    expenses = load_expenses()

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense Added Successfully!")

# View expenses
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No Expenses Found!")
        return

    for e in expenses:
        print(e["date"], "|", e["category"], "| ₹", e["amount"])

# Monthly report
def monthly_report():
    month = input("Enter Month (YYYY-MM): ")

    expenses = load_expenses()

    total = 0

    print("\nExpenses:")
    for e in expenses:
        if e["date"].startswith(month):
            print(e["date"], e["category"], "₹", e["amount"])
            total += e["amount"]

    print("\nTotal Expense = ₹", total)

# Export CSV
def export_csv():
    expenses = load_expenses()

    with open("expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Date", "Category", "Amount"])

        for e in expenses:
            writer.writerow([e["date"], e["category"], e["amount"]])

    print("Exported to expenses.csv")

# Main Menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Report")
    print("4. Export to CSV")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        monthly_report()
    elif choice == "4":
        export_csv()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
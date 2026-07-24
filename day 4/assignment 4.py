import json
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    filename="expense.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        return []
    except Exception as e:
        logging.error(e)
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)

        logging.info("Expense added")
        print("Expense saved successfully")

    except Exception as e:
        logging.error(e)
        print("Invalid input")


def show_expenses():
    expenses = load_expenses()

    for expense in expenses:
        print(expense)


def monthly_report():
    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense:", total)


def export_csv():

    expenses = load_expenses()

    with open("expense_report.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "amount",
                "category",
                "date"
            ]
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("CSV Exported")


while True:

    print("""
1. Add Expense
2. Show Expenses
3. Monthly Report
4. Export CSV
5. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        monthly_report()

    elif choice == "4":
        export_csv()

    elif choice == "5":
        break

    else:
        print("Wrong choice")
import json
import csv

expenses = []

# Expense input
name = input("Enter expense name: ")
amount = input("Enter amount: ")

expense = {
    "name": name,
    "amount": amount
}

expenses.append(expense)

# Save in JSON
with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

print("Expense saved in JSON!")

# Export to CSV
with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Amount"])

    for expense in expenses:
        writer.writerow([
            expense["name"],
            expense["amount"]
        ])

print("Expense saved in CSV!")
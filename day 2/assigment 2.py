balance = 0
history = []

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        history.append(f"Deposited: {amount}")
        print("Amount Deposited Successfully!")
    else:
        print("Invalid Amount")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient Balance")
    elif amount <= 0:
        print("Invalid Amount")
    else:
        balance -= amount
        history.append(f"Withdrawn: {amount}")
        print("Amount Withdrawn Successfully!")

def check_balance():
    print(f"Current Balance: {balance}")

def transaction_history():
    if len(history) == 0:
        print("No Transactions Yet!")
    else:
        print("\nTransaction History:")
        for transaction in history:
            print(transaction)

def message():
    print("Thank You for Using Bank Management System!")

while True:
    print("\n===== Bank Management System =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit()

        elif choice == 2:
            withdraw()

        elif choice == 3:
            check_balance()

        elif choice == 4:
            transaction_history()

        elif choice == 5:
            message()
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please Enter Valid Input")
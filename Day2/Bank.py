balance = 0
history = []

while True:
    print("\n===== Bank Menu =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        history.append(f"Deposited ₹{amount}")
        print("Deposit Successful.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            history.append(f"Withdrawn ₹{amount}")
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    elif choice == "3":
        print("Current Balance: ₹", balance)

    elif choice == "4":
        print("\nTransaction History")
        if len(history) == 0:
            print("No Transactions Yet.")
        else:
            for item in history:
                print(item)

    elif choice == "5":
        print("Thank You for Using the Bank System!")
        break

    else:
        print("Invalid Choice! Try Again.")
balance = 0
history = []

while True:
    ch = input("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit : ")

    if ch == "1":
        a = int(input("Amount: "))
        balance += a
        history.append(f"+₹{a}")

    elif ch == "2":
        a = int(input("Amount: "))
        if a <= balance:
            balance -= a
            history.append(f"-₹{a}")
        else:
            print("Insufficient Balance")

    elif ch == "3":
        print("Balance =", balance)

    elif ch == "4":
        print(history)

    elif ch == "5":
        break
    
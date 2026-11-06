balance = float(input("Enter opening balance: "))
daily_limit = 1000
transactions = []
withdrawn_today = 0


def record_transaction(transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    transactions.append(transaction)


def deposit(amount, balance):
    if amount <= 0:
        print("Invalid amount! Deposit must be positive.")
    else:
        balance += amount
        record_transaction("deposit", amount, balance)
        print("Deposit successful!")

    return balance

def withdraw(amount, balance, withdrawn_today):
    if amount <= 0:
        print("Invalid amount! Withdrawal must be positive.")

    elif amount > balance:
        print("Insufficient balance!")

    elif amount > daily_limit - withdrawn_today:
        print("Daily withdrawal limit exceeded!")

    else:
        balance -= amount
        withdrawn_today += amount

        record_transaction("withdrawal", amount, balance)
        print("Withdrawal successful!")

    return balance, withdrawn_today

def check_balance(balance):
    print(f"Current balance: {balance:.2f} Birr")

def transaction_summary(balance, transactions):
    total_deposited = 0
    total_withdrawn = 0

    for transaction in transactions:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]

        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("\n----- TRANSACTION SUMMARY -----")
    print(f"Total deposited: {total_deposited:.2f} Birr")
    print(f"Total withdrawn: {total_withdrawn:.2f} Birr")
    print(f"Final balance: {balance:.2f} Birr")

    print("\nTransaction History:")

    for transaction in transactions:
        print(transaction)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance = deposit(amount, balance)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        balance, withdrawn_today = withdraw(
            amount, balance, withdrawn_today
        )

    elif choice == "3":
        check_balance(balance)

    elif choice == "4":
        transaction_summary(balance, transactions)

    elif choice == "5":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.")

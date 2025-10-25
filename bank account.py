class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Current Balance:", self.balance)


# ----------- PREDEFINED ACCOUNTS -----------
accounts = {
    "111": BankAccount("111", "John Doe", "2024-01-01", 5000),
    "222": BankAccount("222", "Mary Jane", "2023-06-15", 8000),
    "333": BankAccount("333", "Peter Parker", "2025-03-10", 12000)
}


# ----------- MENU -----------
while True:
    print("\n---- BANK MENU ----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show Customer Details")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice in ["1", "2", "3", "4"]:
        acc_no = input("Enter Account Number: ")

        if acc_no not in accounts:
            print("Account not found!")
            continue  # go back to main menu

        acc = accounts[acc_no]

        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: "))
                acc.deposit(amt)
                print("Deposited:", amt)
            except ValueError:
                print("Invalid amount entered!")

        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: "))
                print(acc.withdraw(amt))
            except ValueError:
                print("Invalid amount entered!")

        elif choice == "3":
            print("Current Balance:", acc.check_balance())

        elif choice == "4":
            acc.customer_details()

    elif choice == "5":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

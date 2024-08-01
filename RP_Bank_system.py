class Bank:
    def _init_(self):
        self.customers = {}

    def create_customer(self, name, account_number, initial_balance):
        self.customers[account_number] = Customer(name, account_number, initial_balance)

    def get_customer(self, account_number):
        return self.customers.get(account_number)


class Customer:
    def _init_(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def borrow(self, amount):
        self.balance += amount
        print(f"Loan approved. New balance: {self.balance}")

    def repay(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Loan repaid. New balance: {self.balance}")


bank = Bank()

while True:
    print("1. Create Customer")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Borrow")
    print("5. Repay")
    print("6. Check Balance")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.create_customer(name, account_number, initial_balance)
    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        customer = bank.get_customer(account_number)
        if customer:
            customer.withdraw(amount)
        else:
            print("Customer not found")
    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        customer = bank.get_customer(account_number)
        if customer:
            customer.deposit(amount)
        else:
            print("Customer not found")
    elif choice == "4":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to borrow: "))
        customer = bank.get_customer(account_number)
        if customer:
            customer.borrow(amount)
        else:
            print("Customer not found")
    elif choice == "5":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to repay: "))
        customer = bank.get_customer(account_number)
        if customer:
            customer.repay(amount)
        else:
            print("Customer not found")
    elif choice == "6":
        account_number = input("Enter account number: ")
        customer = bank.get_customer(account_number)
        if customer:
            print(f"Balance: {customer.balance}")
        else:
            print("Customer not found")
    elif choice == "7":
        break
    else:
        print("Invalid choice")
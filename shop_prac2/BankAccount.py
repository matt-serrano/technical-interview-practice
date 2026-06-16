class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.status = "active"

    def deposit(self, amount):
        if amount <= 0:
            return "Cannot deposit $0 or less!"
        self.balance += amount
        return "Successfully deposited $" + amount + "!"  

    def withdraw(self, amount):
        if self.balance <= 0:
            return "No money to withdraw!"
        self.balance -= amount
        return "Successfully withdrew $" + self.balance + "!"

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def close_account(self):
        if self.account == "inactive":
            return "Account is already closed"
        self.status = "inactive"
        return "Account has been closed"
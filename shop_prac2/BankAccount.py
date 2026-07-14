class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.status = "active"

    def deposit(self, amount):
        if self.status == "closed":
            return "Cannot deposit to a closed account!"
        if amount <= 0:
            return "Cannot deposit $0 or less!"
        self.balance += amount
        return "Successfully deposited $" + str(amount) + "!"  

    def withdraw(self, amount):
        if self.status == "closed":
            return "Cannot withdraw from a closed account!"
        if self.balance <= 0:
            return "No money to withdraw!"
        self.balance -= amount
        return "Successfully withdrew $" + str(amount) + "!"

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def close_account(self):
        if self.status == "closed":
            return "Account is already closed"
        if self.balance > 0:
            return "Cannot close account with money in it!"
        self.status = "closed"
        return "Account has been closed"
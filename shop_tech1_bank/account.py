class Account:
    def __init__(self):
        self._balance = 0.00

    def check_balance(self):
        return f"Balance: ${self._balance}"

    def deposit(self, amt):
        if amt <= 0:
            return f"Cannot deposit money! Invalid amount"
        self._balance += amt
        print(f"Deposited ${amt:.2f}")
        return self.check_balance()

    def withdraw(self, amt):
        if amt <= 0 or amt > self._balance:
            return f"Cannot withdraw money! Invalid amount"
        self._balance -= amt
        print(f"Withdrew ${amt:.2f}")
        return self.check_balance()

    # Incorrect implementation:
    # def withdraw(self, amt):
    #     if amt <= 0 or amt > self._balance:
    #         return f"Cannot withdraw money! Invalid amount"
    #     self._balance += amt
    #     print(f"Withdrew ${amt:.2f}")
    #     return self.check_balance()

    

    

    

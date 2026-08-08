import re # for formatting we use the regular expression module

class Account:
    def __init__(self):
        self._balance = 0.00 # initialize accounts with 0 money

    def check_balance(self):
        return f"Balance: ${self._balance:.2f}" # return the balance in a formatted string

    def deposit(self, amt):
        if not self.is_formatted(amt): # check if the input is in proper money format before doing math
            return f"Cannot deposit money! Invalid amount"
        
        amt = float(amt) # convert string input into a number after we know it looks valid

        if amt <= 0: # edge case to check if the money is 0 or less since you cannot deposit invalid amount
            return f"Cannot deposit money! Invalid amount"
        
        self._balance += amt
        print(f"Deposited ${amt:.2f}")
        return self.check_balance()

    def withdraw(self, amt):
        if not self.is_formatted(amt): # check if the input is in proper money format before doing math
            return f"Cannot withdraw money! Invalid amount"
        
        amt = float(amt) # convert string input into a number after we know it looks valid

        if amt <= 0 or amt > self._balance: # edge case for 0 money or greater than balance
            return f"Cannot withdraw money! Invalid amount"
        
        self._balance -= amt
        print(f"Withdrew ${amt:.2f}")
        return self.check_balance()

    # how do we check if the string input is properly formatted?
    def is_formatted(self, value):
        return bool(re.fullmatch(r"\d+\.\d{2}", value)) # checks for digits, decimal point, then exactly 2 digits

    

    

    

from BankAccount import BankAccount

class BankingSystem:
    def __init__(self):
        self.list_of_accounts = []

    def add_account(self, account):
        self.list_of_accounts.append(account)   

    def get_active_accounts(self):
        return [account for account in self.list_of_accounts if account.get_status() == "active"]
    


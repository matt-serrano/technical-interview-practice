import unitest
from datetime import date

from bank import Bank

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account = BankAccount("John Doe", 1000)

    def test_add_account_to_list_adds_new_account(self):
        self.assertTrue(self.system.add_account(self.account))
        self.assertFalse(self.system.add_account(self.account))
        self.asserEqual(self.system.add_account(self.account))

    def test_get_available
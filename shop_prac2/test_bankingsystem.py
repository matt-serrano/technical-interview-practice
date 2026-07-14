import unittest

from BankAccount import BankAccount
from BankingSystem import BankingSystem


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.system = BankingSystem()
        self.account = BankAccount("ACC-001", "John Doe", 1000)

    def test_new_system_has_no_accounts(self):
        # A new banking system should start with an empty account list.
        self.assertEqual(self.system.list_of_accounts, [])

    def test_add_account_adds_account_to_list(self):
        # Adding an account should store that exact account in the system.
        self.system.add_account(self.account)

        self.assertEqual(self.system.list_of_accounts, [self.account])

    def test_get_active_accounts_returns_active_accounts(self):
        # Accounts are active by default, so an added account should be returned.
        self.system.add_account(self.account)

        self.assertEqual(self.system.get_active_accounts(), [self.account])

    def test_get_active_accounts_excludes_closed_accounts(self):
        # A zero-balance account can be closed and must not appear as active.
        closed_account = BankAccount("ACC-002", "Jane Doe", 0)
        closed_account.close_account()
        self.system.add_account(self.account)
        self.system.add_account(closed_account)

        self.assertEqual(self.system.get_active_accounts(), [self.account])

    def test_get_active_accounts_returns_empty_list_when_none_are_active(self):
        # If every stored account is closed, the active-account list should be empty.
        closed_account = BankAccount("ACC-003", "Sam Lee", 0)
        closed_account.close_account()
        self.system.add_account(closed_account)

        self.assertEqual(self.system.get_active_accounts(), [])


if __name__ == "__main__":
    unittest.main()

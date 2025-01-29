import unittest

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    
    def test_deposit(self):
        account = BankAccount(balance=1000)
        new_balance = account.deposit(500)
        assert new_balance == 1500

        
import unittest

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    """
    Unit tests for the BankAccount class.
    
    Methods
    -------
    setUp():
        Initializes a BankAccount instance with a balance of 1000 for use in tests.
    
    test_deposit():
        Tests that depositing 500 into the account increases the balance to 1500.
    
    test_withdraw():
        Tests that withdrawing 500 from the account decreases the balance to 500.
    
    test_get_balance():
        Tests that the get_balance method returns the correct balance of 1000.
    """
    
    def setUp(self):
        self.account = BankAccount(balance=1000)
    
    def test_deposit(self):
        """
        Tests that depositing 500 into the account increases the balance to 1500.
        """
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        """
        Tests that withdrawing 500 from the account decreases the balance to 500.
        """
        new_balance = self.account.withdraw(500)
        assert new_balance == 500

    def test_get_balance(self):
        """
        Tests that the get_balance method returns the correct balance of 1000.
        """
        assert self.account.get_balance() == 1000
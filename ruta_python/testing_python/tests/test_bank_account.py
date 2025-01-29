import unittest, os

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
    
    test_transaction():
        Tests that a transaction log file is created after a deposit.
    
    test_count_transactions():
        Tests that the number of lines in the transaction log file increases with each transaction.
    """
    
    def setUp(self):
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, file):
        with open(file, 'r') as f:
            return len(f.readlines())
    
    def test_deposit(self):
        """
        Tests that depositing 500 into the account increases the balance to 1500.
        """
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        """
        Tests that withdrawing 500 from the account decreases the balance to 500.
        """
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500, "El balance no es igual")

    def test_get_balance(self):
        """
        Tests that the get_balance method returns the correct balance of 1000.
        """
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def test_transaction(self):
        """
        Tests that a transaction log file is created after a deposit.
        """
        self.account.deposit(500)
        self.assertTrue(os.path.exists('transaction_log.txt'))

    def test_count_transactions(self):
        """
        Tests that the number of lines in the transaction log file increases with each transaction.
        """
        assert self._count_lines('transaction_log.txt') == 1
        self.account.deposit(500)
        assert self._count_lines('transaction_log.txt') == 2
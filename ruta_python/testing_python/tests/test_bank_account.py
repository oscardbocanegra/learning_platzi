import unittest, os
from unittest.mock import patch
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    """
    Unit tests for the BankAccount class.
    
    Methods
    -------
    setUp():
        Initializes a BankAccount instance with a balance of 1000 for use in tests.
    
    tearDown():
        Removes the transaction log file if it exists after each test.
    
    _count_lines(filename):
        Helper method to count the number of lines in a file.
    
    test_deposit_increases_balance_by_deposit():
        Tests that depositing an amount increases the account balance by that amount.
    
    test_deposit_logs_transaction():
        Tests that a transaction log file is created after a deposit.
    
    test_withdraw_logs_each_transaction():
        Tests that the number of lines in the transaction log file increases with each transaction.
    
    test_withdraw_raises_error_when_insufficient_funds():
        Tests that an InsufficientFundsError is raised when attempting to withdraw more than the available balance.
    
    test_withdraw_during_bussines_hours():
        Tests that withdrawing during business hours is allowed.
    
    test_withdraw_disallow_before_bussines_hours():
        Tests that withdrawing before business hours raises a WithdrawalTimeRestrictionError.
    
    test_withdraw_disallow_after_bussines_hours():
        Tests that withdrawing after business hours raises a WithdrawalTimeRestrictionError.
    
    test_deposit_multiple_amounts():
        Tests multiple deposit amounts and verifies the expected balance after each deposit.
    """
    
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_increases_balance_by_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    def test_deposit_multiple_amounts(self):
        test_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            self.account = BankAccount(balance=1000, log_file="transactions.txt")
            with self.subTest(case=case):
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])
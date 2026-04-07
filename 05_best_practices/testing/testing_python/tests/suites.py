import unittest
"""
This module defines a test suite for the BankAccount class.
Classes:
    BankAccountTests: A unittest.TestCase subclass that contains tests for the BankAccount class.
Functions:
    bank_account_suite(): Creates a test suite containing tests for the BankAccount class.
Usage:
    Run this module directly to execute the test suite using unittest's TextTestRunner.
"""

from test_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests('test_deposit'))
    suite.addTest(BankAccountTests('test_withdraw'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError

class BankAccount:
    """
    A class used to represent a Bank Account.
    
    Attributes
    ----------
    balance : float
        The balance of the bank account.
    log_file : str
        The file where transactions are logged.
    
    Methods
    -------
    deposit(amount):
        Deposits a specified amount into the bank account.
    
    withdraw(amount):
        Withdraws a specified amount from the bank account if within business hours and sufficient funds are available.
    
    get_balance():
        Returns the current balance of the bank account.
    
    _log_transaction(message):
        Logs a transaction message to the log file if logging is enabled.
    """
    
    def __init__(self, balance=0, log_file=None):
        """
        Initializes the BankAccount with a balance and an optional log file.
        
        Parameters
        ----------
        balance : float, optional
            The initial balance of the account (default is 0).
        log_file : str, optional
            The file where transactions will be logged (default is None).
        """
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        """
        Logs a transaction message to the log file if logging is enabled.
        
        Parameters
        ----------
        message : str
            The transaction message to log.
        """
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        """
        Deposits a specified amount into the bank account.
        
        Parameters
        ----------
        amount : float
            The amount to deposit.
        
        Returns
        -------
        float
            The new balance after the deposit.
        """
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the bank account if within business hours and sufficient funds are available.
        
        Parameters
        ----------
        amount : float
            The amount to withdraw.
        
        Returns
        -------
        float
            The new balance after the withdrawal.
        
        Raises
        ------
        WithdrawalTimeRestrictionError
            If the withdrawal is attempted outside of business hours (8am to 5pm).
        InsufficientFundsError
            If the withdrawal amount exceeds the available balance.
        """
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self.balance}"
            )
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        """
        Returns the current balance of the bank account.
        
        Returns
        -------
        float
            The current balance of the bank account.
        """
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
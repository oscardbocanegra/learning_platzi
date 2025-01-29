class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(f'{message}\n')

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        elif amount == 0:
            raise ValueError("Amount must be greater than 0")
        elif amount > 0:
            self.balance += amount
            self._log_transaction(f'Deposited: {amount}. New balance: {self.balance}')
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        elif amount < 0:
            raise ValueError("Amount must be positive")
        elif amount == 0:
            raise ValueError("Amount must be greater than 0")
        elif amount > 0:
            self.balance -= amount
            self._log_transaction(f'Withdrawn: {amount}. New balance: {self.balance}')
        return self.balance

    def get_balance(self):
        self._log_transaction(f'Balance checked: {self.balance}')
        return self.balance
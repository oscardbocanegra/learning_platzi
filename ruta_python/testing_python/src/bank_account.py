class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        elif amount == 0:
            raise ValueError("Amount must be greater than 0")
        elif amount > 0:
            self.balance += amount
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
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Balance: {self.balance}"
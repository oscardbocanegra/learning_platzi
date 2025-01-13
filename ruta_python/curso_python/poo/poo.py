class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balace = balance
        self.is_active = True
        
    def deposit(self, amount):
        if self.is_active:
            self.balace += amount
            print(f"Se ha depositado {amount}. Saldo actual es de {self.balace}")
        else:
            print("Cuenta inactiva ")
            
    def withdraw (self, amout):
        if self.is_active:
            if self.balace <= amout:
                self.balace -= amout
                print(f"Se ha retirado {amout}. Tu saldo actual es de {self.balace}")
                
    def deactivate_account(self):
        self.is_active = False
        print(f"Su cuenta ha sido desactivada exitosamente")
        
    def activate_account(self):
        self.is_active = True
        print(f"Su cuenta ha sido activada exitosamente")
        

account1 = BankAccount("Oscar", 10000000)
account2 = BankAccount("Juan", 50000000)

# Llamada de metodos

account1.deposit(5000000)
print(account1.balace)
account2.deposit(1000000)

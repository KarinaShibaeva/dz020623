class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self):
        pass
    
    def withdraw(self):
        pass
    
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        
    def deposit(self):
        print(f"Средства с счета {self.account_number} сняты")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
            
    def withdraw(self):
        print(f"Средства на счет {self.account_number} внесены")
        

m = SavingAccount(1111, 300)

m.deposit()

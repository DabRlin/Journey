class Account:
    def __init__(self,account_number,balance = 0.0) -> None:
        self.account_number = account_number
        self.balance = balance
    
    #存款
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            return True
        return False
    
    #取款
    def withdraw(self,amount):
        if amount>0 and amount<self.balance:
            self.balance -= amount
            return True
        return False
    
    #格式化输出
    def __str__(self) -> str:
        return f"Account:{self.account_number},balance:{self.balance}"

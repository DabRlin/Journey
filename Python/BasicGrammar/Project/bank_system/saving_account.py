from bank_account import BankAccount

class SavingsAccount(BankAccount):
    #添加年利率属性
    def __init__(self, owner, balance=0, interest_rate = 0.02) -> None:
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    #添加利息方法    
    def apply_interest(self):
        interest = self._balance *self.interest_rate
        self.deposit(interest)
        print(f"年利息:{interest},新的余额：{self._balance}")
        
    def account_type(self):
        return "Saving account"
    
    def __str__(self) -> str:
        return super().__str__()+f"\nInterest rate:{self.interest_rate}"
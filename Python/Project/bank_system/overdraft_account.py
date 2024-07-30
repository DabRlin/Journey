from bank_account import BankAccount

class OverdraftAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit = 500) -> None:
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    #实现透支用户的取款
    def withdraw(self, amount):
        if amount > 0:
            if amount <self._balance+self.overdraft_limit:
                self._balance -=amount
                print(f"取款成功：{amount},新的余额：{self._balance}")
            else:
                print("余额与透支余额不足")
        else:
            print("取款金额必须是正数")
    #返回账户类型
    def account_type(self):
        return "Overdraft account"
    #自定义格式化输出
    def __str__(self) -> str:
        return super().__str__()+f"\n透支上限:{self.overdraft_limit}"
from abc import ABC,abstractmethod

class Account(ABC):
    @abstractmethod
    #存款功能
    def deposit(self,amount):
        pass
    @abstractmethod
    #取款功能
    def withdraw(self,amount):
        pass
    @abstractmethod
    #获取余额功能
    def get_balance(self):
        pass
    @abstractmethod
    #返回账户类型功能
    def account_type(self):
        pass

class BankAccount(Account):
    #添加owner和balance分别表示账户所有者和初始余额
    def __init__(self,owner,balance = 0) -> None:
        super().__init__()
        self.owner = owner
        self._balance = balance
    
    #实现取款
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"存入{amount},新的余额{self._balance}")
        else:
            print("存款数额必须是正数")
            
    #实现存款
    def withdraw(self, amount):
        if amount > 0 and self._balance>amount:
            self._balance -= amount
            print(f"取款成功{amount},新的余额：{self._balance}")
        elif self._balance < amount:
            print("余额不足")
        else:
            print("取款数额必须是正数")
            
    #实现返回当前余额
    def get_balance(self):
        return self._balance
    
    #实现返回账户类型
    def account_type(self):
        return "General account"
    
    #自定义格式化输出
    def __str__(self) -> str:
        return f"账户：{self.owner},账户余额：{self._balance}"
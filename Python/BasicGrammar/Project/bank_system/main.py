from bank_account import BankAccount
from overdraft_account import OverdraftAccount
from saving_account import SavingsAccount

def main():
    #创建不同的用户
    general_account = BankAccount("Alice",1000)
    overdraft_account = OverdraftAccount("Bob",9000,400)
    saving_account = SavingsAccount("Bily",7000)
    
    accounts=[general_account,overdraft_account,saving_account]
    
    for account in accounts:
        print(account)
        account.deposit(500)
        account.withdraw(2000)
        if isinstance(account, SavingsAccount):
            account.apply_interest()
        print(f"余额：{account._balance}\n")
        
if __name__ == "__main__":
    main()
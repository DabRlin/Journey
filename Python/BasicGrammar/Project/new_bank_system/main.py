from account import Account
from customer import Customer
from bank import Bank

def main():
    #创建银行
    bank = Bank()
    
    #添加客户
    customer1 = Customer("Alice","123456")
    customer2 = Customer("Bob","654321")
    bank.add_customer(customer1)
    bank.add_customer(customer2)
    
    #创建并添加账户
    account1 = Account("ACC123",1000)
    account2 = Account("ACC456",2000)
    bank.add_account(account1)
    bank.add_customer(account2)    
    
    print(bank)
    
    #存款
    print("\nDepositing 500 to ACC123\n")
    account1.deposit(800)
    print(bank)
    
    #取款
    print("\nWithdrawing 400 from ACC456\n")
    account2.withdraw(400)
    print(bank)    
    
    
if __name__ == "__main__":
    main()
class Bank:
    def __init__(self) -> None:
        self.customers = []
        self.accounts = []
        
    #添加账户
    def add_account(self, accout):
        self.accounts.append(accout)
        
    #添加用户
    def add_customer(self,customer):
        self.customers.append(customer)
        
    #通过用户id寻找用户
    def find_customer_by_id(self,id_number):
        for customer in self.customers:
            if customer.id_number == id_number:
                return customer
        return None
    
    #通过账户号寻找账户
    def find_account_by_number(self,account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    #格式化输出
    def __str__(self) -> str:
        customer_list = "\n".join(str(customer) for customer in self.customers)
        account_list = "\n".join(str(account) for account in self.accounts)
        return f"Banc Customers:{customer_list}\n\nBank Account:{account_list}"
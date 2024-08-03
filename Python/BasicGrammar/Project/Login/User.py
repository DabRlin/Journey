class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
    
    #验证密码
    def check_password(self,password):
        if self.password == password:
            return True
        return False
    
    #定义格式化输出
    def __str__(self) -> str:
        return f"User(username = {self.username})"
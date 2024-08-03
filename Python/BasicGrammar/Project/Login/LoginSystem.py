from User import User
from PassWorderror import PasswordError

#采用字典来存储用户信息
class LoginSystem:
    def __init__(self) -> None:
        self.users = {}
        
    def add_user(self,username,password):
        if username not in self.users:
            self.users[username] = User(username,password)
            
    def login(self,username,password):
        if username in self.users:
            user = self.users[username]
            if user.check_password(password):
                print(f"Login successfully for user:{username}")
            else:
                raise PasswordError()
        else:
            print(f"User {username} does not exist")
        
    def __str__(self) -> str:
        userlist = "\n".join(str(user) for user in self.users.values())
        return f"Users:\n{userlist}"
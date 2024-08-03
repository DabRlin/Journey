from LoginSystem import LoginSystem
from PassWorderror import PasswordError
from User import User

def main():
    #创建系统
    login_system = LoginSystem()
    
    #添加用户
    login_system.add_user("alice","password123")
    login_system.add_user("Bob","securepassword")
    
    #打印用户
    print(login_system)
    
    #尝试登录
    try:
        login_system.login("Alice","password123")
        login_system.login("Bob","wrongpasword")
    except PasswordError as e:
        print(e)
        
    try:
       login_system.login("Chris","password123")
    except PasswordError as e:
        print(e)
    except Exception as e:
        print(e) 
        
if __name__ == "__main__":
    main()
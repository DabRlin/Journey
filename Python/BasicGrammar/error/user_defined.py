#自定义异常
class MyError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)
    def __str__(self) -> str:
        return f"MyErrot:{self.message}"

try:
    raise MyError("这是一个异常")
except MyError as e:
    print(e)
    
#创建自定义异常
class MyCustomError(Exception):
    pass

#使用自定义异常
try:
    raise MyCustomError("这是一个自定义异常")
except MyCustomError as e:
    print("捕获的异常:",e)
    
#带有初始化的自定义异常
class MyCustomError(Exception):
    def __init__(self, message, error_code) -> None:
        self.error_code = error_code
        super().__init__(message)
    
try:
    raise MyCustomError("这是一个带有初始化的自定义异常",404)
except MyCustomError as e:
    print(f"捕获的异常：{e},捕获异常的错误代码：{e.error_code}")
    
# 异常的继承
# 捕获并处理多个自定义异常
class NetWorkError(Exception):
    pass

class TimeourError(NetWorkError):
    pass

class ConnectionError(NetWorkError):
    pass

# 模拟网络错误
def perform_network_operation():
    raise TimeourError("操作超时")

try:
    perform_network_operation()
except TimeourError as e:
    print("请求超时：",e)
except ConnectionError as e:
    print("连接错误：",e)
except NetWorkError as e:
    print("网络错误：",e)
    
    
#基本继承异常
class AppError(Exception):
    pass
class FileNotFoundError(AppError):
    pass
class PermissionError(FileNotFoundError):
    pass

try:
    raise FileNotFoundError("未找到此文件")
except AppError as e:
    print("应用错误：",e)
    
# 自定义异常的使用场景
# 验证用户输入
class InvalidInputError(Exception):
    def __init__(self, input_value) -> None:
        super().__init__(f"Invalid input: {input_value}")
        self.input_value = input_value
    
def process_input(input_value):
    if not isinstance(input_value,int):
        raise InvalidInputError(input_value)
    return input_value*2

try:
    result = process_input("ABC")
except InvalidInputError as e:
    print("输入错误：",e)
    
        

#数据库操作
class DatabaseConnectionError(Exception):
    def __init__(self,db_name) -> None:
        super().__init__(f"无法连接到数据库：{db_name}")
        self.db_name = db_name

def connect_to_database(db_name):
    raise DatabaseConnectionError(db_name)

try:
    connect_to_database("example_db")
except DatabaseConnectionError as e:
    print("数据库连接错误:",e)
    

#验证用户登录
class LoginError(Exception):
    def __init__(self, key) -> None:
        super().__init__("密码错误！")
        self.key = key

def Login(key):
    if key != 123456:
        raise LoginError(key)
    print("登录成功!")
#正确密码登录
try:
    Login(123456)
except LoginError as e:
    print(e)
#错误密码登录
try:
    Login(12345)
except LoginError as e:
    print(e)
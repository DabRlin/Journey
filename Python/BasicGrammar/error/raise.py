# raise抛出异常
# 抛出内置异常
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a / b

try:
    result = divide(10,0)
except ZeroDivisionError as e:
    print(e)
    
# 抛出自定义异常
class InvalidAgeError(Exception):
    def __init__(self,age,message="年龄不合法") -> None:
        self.age = age
        self.message = message
        super().__init__(message)
def set_age(age):
    if age <0 or age>100:
        raise InvalidAgeError(age)
    print("年龄设置为：",age)
try:
    set_age(-1)
except InvalidAgeError as e:
    print(f"错误：{e.message},输入的年龄：{e.age}")


# 重新引发异常
# 有时候你捕获一个异常并处理了一部分后，
# 可能还需要将它重新引发给上层代码进行进一步处理。
# 可以使用 raise 关键字重新引发捕获的异常。
file = None
def process_file(filename):
    try:
        file = open(filename,"r")
        data = file.read()
        if "error" in data:
            raise ValueError("文件内容不合法")
    except FileNotFoundError as e:
        print("文件未找到：",e)
        raise
    except ValueError as e:
        print("处理文件时候发生错位：",e)
        raise
    finally:
        file.close()
try:
    process_file("example.txt")
except Exception as e:
    print("捕获到的异常：", e)

#多层次异常处理
class DatabaseError(Exception):
    pass

class ConnetionError(Exception):
    pass

class QueryError(Exception):
    pass

def connect_to_database():
    raise ConnetionError("数据库连接错误")

def execute_query():
    try:
        connect_to_database()
    except ConnetionError as e:
        print("处理链接错误：",e)

def main():
    try:
        execute_query()
    except DatabaseError as e:
        print("数据库操作失败",e)
    
main()
#异常处理
try :
    #可能引发异常的语句
    pass
except FileNotFoundError:
    ##异常1的处理代码
    pass
except ZeroDivisionError:
    #异常2的处理代码
    pass
else:
    #无异常发生执行的代码
    pass
finally:
    #不论如何都会执行的代码
    pass

#异常的捕获
try:
    x = 1/0
except ZeroDivisionError as e:
    print("除零错误：",e)
    
#无异常执行else
try:
    x = 1/1
except ZeroDivisionError as e:
    print("除零错误：",e)
else:
    print("无异常")
    
#finally无论如何都执行
file = None
try:
    file = open("example.txt","r")
    data = file.read()
except FileNotFoundError:
    print("文件未找到")
finally:
    if file:
        file.close()
    
#自定义异常
class MyCustomError(Exception):
    """这是一个自定义异常类"""
    pass

try:
    raise MyCustomError("发生了一个自定义异常")
except MyCustomError as e:
    print(e)
    
#多重异常处理
try:
    x = int("abc")
except(ValueError,TypeError) as e:
    print("发生了错误：",e)

#多个except块
try:
    num = int(input("请输入一个数字:"))
    result = 10 / num
except ValueError:
    print("输入不是有效数字")
except ZeroDivisionError:
    print("除数不能为零")
except Exception as e:
    print("其他错误：",e)
else:
    print("结果是：",result)
finally:
    print("程序执行完毕")
 
#在一个except块中捕获多种异常
try:
    num = int(input("请输入一个数字:"))
    result = 10/num
except(ValueError,ZeroDivisionError) as e:
    print("发生错误:",e)
else:
    print("结果是：",result)
finally:
    print("程序执行完毕")
    
#捕获Exception派生的所有异常
try:
    i = 1/0
except Exception as e:
    print("发生了异常")
    
#自定义异常的多重捕获
class CustomError1(Exception):
    pass
class CustomErrot2(Exception):
    pass
#创建函数抛出异常
def risky_function():
    raise CustomError1("这是自定义错误1")
try:
    risky_function()
except CustomError1:
    print("处理自定义错误1")
except CustomErrot2:
    print("处理自定义错误2")
except Exception as e:
    print("其他错误",e)
finally:
    print("程序执行完毕")
    
#异常信息
try:
    1/0
except ZeroDivisionError as e:
    print("异常类型：",type(e))
    print("异常信息：",e)

#traceback模块获取详细异常信息
import traceback

try:
    1/0
except ZeroDivisionError as e:
    print("完整异常堆栈信息:")
    traceback.print_exc()
       
#自定义异常并传递参数
class MyCustomError(Exception):
    def __init__(self, message, error_code) -> None:
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

try:
    raise MyCustomError("发生了一个自定义错误",404)
except MyCustomError as e:
    print("错误信息:",e.message)
    print("错误代码：",e.error_code)
    
#访问异常对象的属性
class MyError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        #调用父类的构造函数，从而使得MyError类可以利用Exception的所有功能
        super().__init__(self.message)

# 如果你定义了一个自定义异常类，并且传递了一个消息参数，那么 print(e) 也会输出这个消息
try:
    raise MyError("这是一个错误")
except MyError as e:
    print("异常参数：",e.args)
    print("异常信息：",e.message)
    print("字符串表示：",str(e))

#重写__str__方法自定义输出
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

#BaseException继承
class MyBaseError(BaseException):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)
try:
    raise MyBaseError("这是一个错误")    
except MyBaseError as e:
    print("捕获到的异常：",e)
    
#捕获BaseException派生的所有异常
# 捕获 BaseException 是不常见的做法，
# 因为它会捕获系统退出类异常，这可能会干扰程序的正常退出过程。
# 例如，捕获 KeyboardInterrupt 会让用户无法使用 Ctrl+C 终止程序。
try:
    pass
except BaseException as e:
    print("捕获到的异常：",e)

#Python异常层次:
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |    |    +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning
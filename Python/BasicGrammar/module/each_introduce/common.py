#将互相依赖的内容发在一个单独的模块里
#定义成接口或者抽象基类
#让其他模块实现这些接口或者继承这些类

#定义一个抽象基类
#定义了一个方法method抛出异常
#如果子类没有实现method，就会抛出NotImplementedError异常
class CommonInterface:
    def method(self):
        raise NotImplementedError
    
# NotImplementedError 是 Python 中的一个内置异常
# 用于指示某个方法或功能在当前实现中尚未完成或未实现。
# 当你定义一个方法或类时，如果你希望子类实现它
# 你可以使用 NotImplementedError 来表示这个方法需要在子类中进行实现。
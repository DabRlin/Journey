#定义功能
#也会导致循环导入
# def func_a():
#     print("Function A")
#     #延迟导入
#     from module_b import func_b
#     func_b()
    
#导致循环导入
# from module_b import func_b
# def func_a():
#     print("Function A")
#     func_b()

from common import CommonInterface

class A(CommonInterface):
    def method(self):
        pass
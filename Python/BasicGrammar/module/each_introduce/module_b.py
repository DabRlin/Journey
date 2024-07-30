#也会导致循环导入
# def func_b():
#     print("Function B")
#     from module_a import func_a
#     func_a()

# 导致循环导入
# from module_a import func_a
# def func_b():
#     print("Function B")
#     func_a()

from common import CommonInterface
class A(CommonInterface):
    def method(self):
        pass
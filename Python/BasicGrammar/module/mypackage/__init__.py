#导入包时输出
print("Initializing mypackage")

#导入模块的函数
from .module1 import func1
from .module2 import func2

#显式定义from mypackage import *导入的模块和函数
__all__ = ["func1","func2"]

func1 = func1
func2 = func2
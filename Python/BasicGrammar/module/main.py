#导入模块
import mymodule
import mypackage.module1
#调用模块中的功能
mymodule.greet("Alice")

#具体导入模块中的特定成员
from mymodule import greet

greet("Alice")

#导入模块并重命名
import mymodule as mm

mm.greet("Bob")

#导入包
from mypackage import module1,module2
module1.func1()
module2.func2()

#导入整个包
import mypackage
mypackage.module1.func1()

#导入包中特定模块
from mypackage import module1
module1.func1()

#导入模块中的特定成员
from mypackage.module1 import func1
func1()

#导入pip中安装的包
import requests
response = requests.get("http://chatgpt.com")

#编写__init__,导入包时能直接调用func1()
from mypackage import *
func1()

#向__init__中添加func1 = func1
import mypackage
mypackage.func1()
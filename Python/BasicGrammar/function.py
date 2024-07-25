#问候函数
def greet (name):
    print(f"Hello,{name}")

name1 = "Alice" 
greet(name1)

#求和函数
def add (a,b):
    return  a + b
result = add(2,5)
print(result)

#设定默认值
def greet (name = "Alice"):
    print("Hello,{}".format(name))
greet()

#关键字传参
def greet(name, message):
    print(f"{message},{name}!")
greet(message="hello",name="Alice")

# *args
# * 用于将多个位置参数打包成一个元组。
# *args 是用来接收任意数量的位置参数，返回一个包含所有位置参数的元组。
# 在函数定义中，*args 用于接收任意数量的位置参数。
# **kwargs
# ** 用于将多个关键字参数打包成一个字典。
# **kwargs 是用来接收任意数量的关键字参数，返回一个包含所有关键字参数的字典。
# 在函数定义中，**kwargs 用于接收任意数量的关键字参数。

#可变长度参数
def func(*args,**kwargs):
    print("args:, ", args)
    print("kwargs:",kwargs)
func(1,2,3,a = 4,b = 5)

#返回值
def add_substract(a,b):
    return a+b,a-b
result = add_substract(4,5)
print(result)

#匿名函数
add = lambda x,y:x+y
print(add(2,3))

#递归函数
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#函数注释
def add(a:int,b:int):
    return a+b
print(add(3,5))
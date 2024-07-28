#装饰器
#基础装饰器
def decorator (func):
    def wrapper(*args, **kwargs):
        print("something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("something is happening after the function is called.")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Alice")

#带参数的装饰器
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=9)
def greeting(name):
    print(f"Hello,{name}!")

greeting("Alice")

#类装饰器
#--等学到类和对象

#多个装饰器
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        result = func(*args, **kwargs)
        print("Decorator 1 after")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        result = func(*args, **kwargs)
        print("Decorator 2 after")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"Hello,{name}!")
    
say_hello("Alice")

#保留原函数的元数据
#--等学到类和对象

#property内置函数创建和管理类的属性
#目的是简化代码的使用和维护，本质是封装

# property 是一个内置函数，用于创建和管理类的属性。
# 它提供了一种优雅的方式来定义属性的访问和修改方法（getter、setter、deleter）
# 从而允许控制对类属性的访问和修改，同时保持面向对象编程的封装性。

#使用property函数
class MyClass:
    def __init__(self,value) -> None:
        self._attribute = value
        
    def get_attribute(self):
        return self._attribute
    
    def set_attribute(self,value):
        self._attribute = value
    
    def del_attribute(self):
        del self._attribute
        
    attribute = property(get_attribute,set_attribute,del_attribute,"This is a property")
    
#创建实例
obj = MyClass(10)

#访问属性
print(obj.attribute)

#修改属性
obj.attribute = 20
print(obj.attribute)

#删除属性
del obj.attribute

#使用property装饰器
class MyClass:
    def __init__(self,value) -> None:
        self._attribute  = value
    @property
    def attribute(self):
        """This is the getter method"""
        return self._attribute
    @attribute.setter
    def attribute(self,value):
        """This is the setter method"""
        self._attribute = value
    @attribute.deleter
    def attribute(self):
        """This is the deleter method"""
        del self._attribute
        
#创建实例       
obj = MyClass(10)

#访问属性
print(obj.attribute)

#修改属性
obj.attribute = 20
print(obj.attribute)

#删除属性
del obj.attribute
#创建类
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello,my name is {self.name}, i am {self.age} years old")

#创建对象
#类的实例就是对象
person1 = Person("Alice", "18")
person2 = Person("Bob", 14)

#调用类的方法
person1.greet()
person2.greet()

#调用类的属性
print(person2.age)
print(person1.name)

#类的属性和方法
class Car :
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota","Camry",2020)
print(car1.make,car1.model,car1.year)#输出实例属性

class Dog:
    def __init__(self,name) -> None:
        self.name = name
    def bark(self):
        print(f"{self.name} say woof!")

dog1 = Dog("Buddy")
dog1.bark()#调用实例方法

#类属性和类方法初学
class Animal:
    species = "Mammal"
    
    @classmethod
    def get_species(cls):
        return cls.species

print(Animal.get_species())

#类属性和类方法
#类属性
class MyClass:
    class_attribute = "I am a class attribute"
#访问类属性
print(MyClass.class_attribute)
#创建实例
instance1 = MyClass()
print(instance1.class_attribute)

#修改类属性
MyClass.class_attribute = "Hello world"
print(instance1.class_attribute)

#实例属性
class MyClass:
    def __init__(self,value) -> None:
        self.instance_attribute = value
#创建实例并初始化实例属性
instance1 = MyClass("Instance1 attribute")
print(instance1.instance_attribute)
#修改实例属性
instance1.instance_attribute = "Change Instance1 attribute"
print(instance1.instance_attribute)

#类方法
class MyClass:
    class_attribute = "I am a class attribute"
    #创建类方法，接收cls作为第一个参数，表示类本身
    @classmethod
    def class_method(cls):
        return f"Class method called. Class attribute:{cls.class_attribute}"
print(MyClass.class_method())

instance2 = MyClass()
print(instance2.class_method())

#实例方法
class MyClass:
    def __init__(self,value="Instance attribute") -> None:
        self.instance_attribute = value
    #创建实例方法，接收self作为第一个参数
    def instance_method(self):
        return f"Instance method called. Instance attribute:{self.instance_attribute}"
instance3 = MyClass("Instance attribute")
print(instance3.instance_method())

#静态方法&静态属性
#静态方法
class MyClass:
    #创建静态方法，不接受cls或者self的参数，不能方位类属性和实例属性
    @staticmethod
    def static_method():
        return "Static method called"
#调用静态方法
print(MyClass.static_method())
instance4 = MyClass()
print(instance4.static_method())

#静态属性
class MyClass:
    _static_attribute = "I am a static attribute"
    @staticmethod
    def _get_static_attribute():
        return MyClass._static_attribute
    def _set_static_attribute(value):
        MyClass._static_attribute = value
        
    static_attribute = property(_get_static_attribute,_set_static_attribute)
#访问静态属性
print(MyClass.static_attribute)
#修改静态属性
MyClass.static_attribute = "Hello world"
print(MyClass.static_attribute)
#创建实例
instance5 = MyClass()
print(instance5.static_attribute)

#property调用静态方法时候会被仿作实例方法调用，导致接受额外参数
class MyClass:
    _static_attribute = "I am a static attribute"
    @classmethod
    def _get_static_attribute(cls):
        return cls._static_attribute
    @classmethod
    def _set_static_attribute(cls, value):
        cls._static_attribute = value
        
    static_attribute = property(_get_static_attribute,_set_static_attribute)
    
print(MyClass.static_attribute)

#创建实例
instance1 = MyClass()
MyClass.static_attribute = "New value"
print(MyClass.static_attribute)
print(instance1.static_attribute)
    

#静态方法
class Math:
    @staticmethod
    def add(x,y):
        return x+y

print(Math.add(5,7))

#继承和多态
#基础继承
class Animal:
    def __init__(self,name) -> None:
        self.name = name
        
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

dog1 = Dog("Buddy")
cat1 = Cat("Merry")
print(dog1.name)
print(cat1.name)
print(dog1.speak())
print(cat1.speak())
    
#super()函数
class Animals:
    def __init__(self,name) -> None:
        self.name = name

class Dog(Animal):
    def __init__(self, name,breed) -> None:
        super().__init__(name)
        self.breed = breed
        
    def describe(self):
        return f"{self.name} is a {self.breed}"

dog1 = Dog("Buddy","Golden Retriever")
print(dog1.describe())

#多重继承
class Flyable:
    def fly(self):
        return "Flying"
    
class Swimmable:
    def swim(self):
        return "Swimming"
    
class Duck(Flyable,Swimmable):
    def quack(self):
        return "Quack!"
    
duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())

#多态
class Animal:
    def make_sound(self):
        return "Some sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
def print_animal_sound(animal):
    print(animal.make_sound())

dog1 = Dog()
cat1 = Cat()
print_animal_sound(dog1)
print_animal_sound(cat1)

#鸭子类型
class Bird:
    def fly(self):
        print("Flies high")

class Airplane:
    def fly(self):
        print("Flying in the sky")
        
def let_it_fly(fly):
    fly.fly()
    
bird = Bird()
airplane = Airplane()

let_it_fly(bird)
let_it_fly(airplane)

#使用抽象基类来实现接口多态实现抽象基类
# 子类必须实现所有的抽象方法，否则子类也将被视为抽象类，无法实例化。
from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
    def description(self):
        return "This is a shape"
        
class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        
    def area(self):
        return self.height*self.width
    
    def description(self):
        return "This is a rectangle"
    
def print_area(shape):
    print(shape.area())
    
circle = Circle(8)
rectangle = Rectangle(4,6)

print(print_area(circle))
print(print_area(rectangle))
print(circle.description())
print(rectangle.description())

#封装
class Dog:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.age = age
    def get_name(self):
        return self.__name

dog1 = Dog("Buddy",4)
print(dog1.get_name())
#通过名称改写实现访问
class MyClass:
    def __init__(self) -> None:
        self.__private_attr = "This is a private attribute"
obj = MyClass()
#__双下划线前缀将原属性改写名称为_ClassName__attributeName，可通过改写名称直接访问
print(obj._MyClass__private_attr)


#构造函数
#创建对象时自动调用构造函数
class MyClass:
    def __init__(self) -> None:
        print("This is the constructor.")

obj = MyClass()

class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        
person1 = Person("Alice",23)
person2 = Person("Bob",55)
print(person1.age)
print(person2.name)

#默认参数
class Worker(Person):
    def __init__(self, name: str, age: int, job="Teacher") -> None:
        super().__init__(name, age)
        self.job = job

work1 = Worker("Carry",9,"programer")
work2 = Worker("David",9)
print(work1.job)
print(work2.job)

#构造函数中的逻辑
class Rectangle:
    def __init__(self,width, height) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be postive.")
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
rect1 = Rectangle(4,5)
print(rect1.area())
# rect2 = Rectangle(0,0)

#多个构造函数(重载)
#Python不原生支持重载
class Book:
    def __init__(self,title,author,pages = None) -> None:
        self.title = title
        self.author = author
        self.pages = pages if pages is not None else "Unkown"
book1 = Book("Hello world","David",93)
book2 = Book("White house","Steven")
print(book1.pages)
print(book2.pages)
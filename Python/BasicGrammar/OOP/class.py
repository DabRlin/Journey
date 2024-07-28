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

#类属性和类方法*****

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
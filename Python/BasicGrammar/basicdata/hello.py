print("hello world\n")
name = input("请输入你的名字：")
print(f"你好，{name}!")
x  = 12
print("the number is",x)
print("hello","world")
name = "alice"
age = 25
name2 = "Bob"
age2 = 12
print("Name: %s, Age: %d"%(name,age))
print("Name: {}, Age: {}".format(name2,age2))
print("Name: {1}, Age: {0}".format(name2,age2))
print("Name: {name}, Age: {age}".format(name = name2,age = age2))
print(f"Name: {name}, Age: {age}")
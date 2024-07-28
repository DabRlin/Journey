#字符串转化为整形
x= "123"
y = int(x)
print(x,y,type(x),type(y))

#整形转化为字符串
x = 123
y = str(x)
print(x,y,type(x),type(y))

#元组转化为列表
x = {1,2,3}
y = list(x)
print(x,y,type(x),type(y))

#列表转化为元组
x = [1,2,3,4]
y = tuple(x)
print(x,y,type(x),type(y))

#列表转化为集合
x = [1,2,2,4]
y = set(x)
print(x,y,type(x),type(y))

#键值对转化为字典
x = [("name","Alice"),("age",24)]
y = dict(x)
print(x,y,type(x),type(y))

#数值转化为布尔
x = 1
y = bool(x)
print(x,y,type(x),type(y))
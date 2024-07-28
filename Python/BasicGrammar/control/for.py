#for遍历

#for遍历list
numbers = [1,3,4,5,6]
for i in numbers:
    print(i)
    
#for遍历字符串
for i in "hello":
    print(i)
    
#for遍历集合
num = {1,2,3,5,6}
for i in num:
    print(i)
    
#for遍历字典
dir = {"name":"alice","age":"19"}
for i in dir:
    print(i)
    
#遍历从零到四整数序列
for i in range(8):
    print(i)

#遍历从1到19整数序列
for j in range(1,19):
    print(j)
    
#遍历从1到123，步长为5的整数序列
for k in range(1,123,5):
    print(k)
    
#break跳出循环
for w in range (10):
    if w == 5:
        break
    print(w)

#continue进入下一次循环
for w in range(2,10):
    if w == 4:
        continue
    print(w)

#pass语法占位符
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
        
#列表推导式代替for循环
square = []
for x in range(10):
    square.append(x**2)

squares = [x**2 for x in range(10)]
print(square)
print(squares)

#条件表达式
x = 10
result = "greater than 5"if x > 5 else "less or equal to 5"
print(result)

#for搭配else进行使用
for i in range(10):
    print(i)
else:
    print("hello world")
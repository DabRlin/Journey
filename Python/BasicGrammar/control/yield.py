#yield定义生成器函数，返回函数生成对象

def count_up_to(max):
    count = 1
    while count < max:
        yield count
        count += 1
        
for number in count_up_to(5):
    print(number)
    
num = count_up_to(9)
print(num)
for value in num:
    print(value)
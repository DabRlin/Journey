#迭代器iterator
class MyIterator:
    def __init__(self,start,end) -> None:
        self.current = start
        self.end = end
        
    #使对象本身变为可迭代对象，可以被for循环或其他迭代上下文使用
    def __iter__(self):
        return self
    
    #返回迭代器的下一个元素，每次调用返回一个新的值，直到没有更多元素
    def __next__(self):
        if self.current >= self.end:
            #内置异常，标识迭代结束
            raise StopIteration
        else:
            self.current += 1
            return self.current-1

#创建迭代器实例
my_iter = MyIterator(1,9)

#for循环自动遍历
for num in my_iter:
    print(num)
print(my_iter)

#while循环手动遍历
while True:
    try:
        num = next(my_iter)
        print(num)
    #捕获异常退出
    except StopIteration:
        break
    
#生成器generator
def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current +=1
    
#for自动迭代    
for num in my_generator(0,4):
    print(num)
    
#while手动迭代
gen = my_generator(0,5)

while True:
    try:
        value = next(gen)
        print(value)
    except StopIteration:
        break
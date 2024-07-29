#文件操作

#读文件
#open打开文件
file = open("Python/BasicGrammar/file/example.txt",'r')
#读取整个文件
content = file.read()
#读取文件某一行
line = file.readline()
#读取所有行
lines = file.readlines()
file.close()

print(content)
print(line)
print(lines)

#写文件
file = open("Python/BasicGrammar/file/example.txt",'w')
#写入字符串
file.write("Hello world!\n")
#写入字符串列表
file.writelines(["Hello world!\n","Python File Operations\n"])
file.close()

#with语句打开文件
#可以保证文件在使用完毕后正确关闭
with open("Python/BasicGrammar/file/example.txt",'r') as file:
    content = file.read()
    
with open("Python/BasicGrammar/file/example.txt",'w') as file:
    file.write("nihao, world!")
    
with open("Python/BasicGrammar/file/example.txt",'rb') as file:
    #返回当前位置
    print(file.tell())
    #移动当前位置
    file.seek(0)
    file.seek(10,1)
    file.seek(-10,2)
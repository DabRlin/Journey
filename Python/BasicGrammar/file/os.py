#导入os模块
import os

#创建文件
with open("Python/helo.txt","w") as file:
    print(file.tell())
    
#重命名文件
os.rename("Python/hello.py","Python/hello.py")

#删除文件
os.remove("Python/helo.txt")

#创建文件夹
os.mkdir("new_dir")
os.mkdir("new_dir2")

#删除文件夹
os.remove("new_dir2")

#获取文件属性
file_stat = os.stat("Python/hello.py")
print(file_stat.st_size)
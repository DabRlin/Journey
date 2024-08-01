#用于FTP协议的客户端操作
#导入模块
from ftplib import FTP

#创建FTP对象并连接到服务器
ftp = FTP('chatgpt.com')

#登录服务器，需要使用实际连接到FTP服务器地址
ftp.login(user='username', passwd='password')

#改变当前目录到上传文件的目录
ftp.cwd('path/to/directory')

#打开文件读取
with open('file.txt','rb') as file:
    #将打开的文件上传到FTP服务器
    ftp.storbinary("STOR file.text",file)

#退出FTP连接
ftp.quit()

#同上
ftp = FTP('ftp.example.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/path/to/directory')
#下载文件
with open('file.txt', 'wb') as file:
    #file.write是一个回调函数，将FTP服务器传输的数据写入到本地文件
    ftp.retrbinary('RETR file.txt', file.write)
ftp.quit()
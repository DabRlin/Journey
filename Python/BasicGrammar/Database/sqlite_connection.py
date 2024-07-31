#Python连接SQLite数据库
#导入连接数据库的相关包
import sqlite3

#连接数据库
conn = sqlite3.connect("C:/Users/dangh/Downloads/Journary/Python/BasicGrammar/Database/mydatabase.db")

#创建游标
cursor = conn.cursor()

#使用游标执行sql查询语句
cursor.execute("SELECT * FROM users")

#打印结果
#cursor.fetchall:获取所有查询结果并返回一个列表
result = cursor.fetchall()
for row in result:
    print(row)
    
#关闭游标，释放与数据库交互的资源
cursor.close()
#关闭数据库连接，释放与使劲哭服务器的连接资源
conn.close
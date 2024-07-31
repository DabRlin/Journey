#Python连接MySQL数据库
import mysql.connector

#连接到数据库
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'chy2293849140',
    database = 'journary' 
)

#创建游标，游标是用来执行SQL语句并获取结果的对象。
#创建游标后可以使用游标来执行各种SQL语句
cursor = conn.cursor()

#使用游标执行查询语句
cursor.execute("SELECT * FROM students")

#打印结果
result = cursor.fetchall()
for row in result:
    print(row)

#关闭游标
cursor.close()
#关闭数据库连接
conn.close()
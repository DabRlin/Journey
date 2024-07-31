import sqlite3

#定义用户类
class User:
    def __init__(self, id = None, name = None, age = None, email = None) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.email = email
    
    #定义静态方法不依赖实例
    @staticmethod
    #返回sqlite连接
    def connect():
        return sqlite3.connect("C:/Users/dangh/Downloads/Journary/Python/BasicGrammar/Database/user_test_sqlite/mydatabase.db")
        
    @staticmethod
    #创建表如果不存在
    def create_table():
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute('''
        create table if not exist user(
            if integer primary key autoincrement,
            name text,
            age integer,
            email text
        )''')
        conn.commit()
        conn.close()
    
    #实现添加行或者更新行    
    def save(self):
        conn = User.connect()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
            insert into user (name, age, email) values (?, ?, ?)
            ''',(self.name,self.age,self.email))
        else:
            cursor.execute('''
            update user set name = ?,age = ?, email = ? where id = ?
            ''',(self.name,self.age,self.email,self.id))
        conn.commit()
        conn.close()
        
    @staticmethod
    #通过id查找用户
    def get_by_id(user_id):
        conn = User.connect()
        cursor = conn.cursor()
        #圆括号中如果只有一个元素，加上逗号才表示元组，否则只是一个括号
        cursor.execute('select * from user where id = ?',(user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(*row)
        return None
    
    @staticmethod
    #通过id删除用户
    def delete_by_id(user_id):
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute("delete from user where id = ?",(user_id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    #获取所有用户
    def get_all():
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute("select * from user")
        rows = cursor.fetchall()
        conn.close()
        return [User(*row) for row in rows]
    
    #自定义格式化输出
    def __repr__(self) -> str:
        return f"User(id = {self.id}), age = {self.age}, email = {self.email})"
    
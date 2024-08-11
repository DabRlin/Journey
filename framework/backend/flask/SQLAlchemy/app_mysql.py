from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql://username:password@localhost/db_name"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
#如果安装了pymysql，可以使用代替sqlclient
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'


#Plan A 在模型类中封装CRUD操作
# 模型类方法：适合小型项目，方便快速开发
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable = False)
    email = db.Column(db.String(20),unique = True,nullable = False)
    password = db.Column(db.String(60),nullable = False)
    
    #Create a new user
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    #Read a user by id
    @classmethod
    #创建类方法，接收cls第一个参数表示类本身
    def get_by_id(cls,user_id):
        #query.get:通过主键获取单条记录
        return cls.query.get(user_id)
    
    #Read all users
    @classmethod
    def get_all(cls):
        #query.all:获取查询的所有结果
        return cls.query.all()
    
    #update the user
    def update(self,**kwargs):
        #key参数名 value对应的值
        for key, value in kwargs.items():
            #使用setattr在self对象上设置属性 若属性名不存在则创建属性 存在则赋值
            setattr(self,key,value)
        db.session.commit()
        
    #delete the user
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
#Plan B 创建一个通用的CRUD类
# 通用CRUD类：适合需要多个模型复用的情况，简化代码。
class CURDMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_by_id(cls,id):
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    def update(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
#继承CRUDMixin
class User(db.Model, CURDMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable = False)
    email = db.Column(db.String(120),unique = True,nullable = False)
    password = db.Column(db.String(60),nullable = False)
    
#Plan C 使用服务层进行封装
# 服务层封装：适合大型项目，将业务逻辑与数据模型分离，便于维护和扩展。
class UserService:
    @staticmethod
    def create_user(username,email,password):
        user = User(username = username,email = email,password = password)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def update_user(user,**kwargs):
        for key, value in kwargs:
            setattr(user,key,value)
        db.session.commit()
            
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
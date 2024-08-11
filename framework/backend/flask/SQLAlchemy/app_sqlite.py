from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = (__name__)

#连接数据库
#sqlalchemy_database_url:指定数据库的url
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

#禁用信号追踪
app.config["SQLALCHEMY_TRACK_MODIFICATIOINS"]=False
#将Flask应用实例传递给SQLAlchemy
db = SQLAlchemy(app)

#定义模型类
class User(db.Model):
    #定义每一列
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable =False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    #定义user和posts一对多的关系，使用backref创建一个虚拟列从而直接通过post.author访问User
    #lazy懒加载：相关数据在访问时才加载
    posts = db.relationship("Post",backref="author",lazy="True")
    
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    #设置默认事件为当前的UTC时间
    date_posted = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)
    content = db.column(db.Text,nullable = False)
    #定义外键
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    
    # 生成数据库表：当你调用 db.create_all() 时，
    # SQLAlchemy 会读取所有已经定义的模型类，并为这些模型类自动创建对应的数据库表。
    # 如果表不存在，它们将被创建；如果已经存在，它们不会被重新创建。
    
#创建应用上下文来访问应用配置，数据库操作所需要的信息都存放在上下文中
with app.app_context():
    db.create_all()

#创建新用户
new_user = User(username="JohnDoe",email="Jane@example.com")
#db.session会话对象，提供处理对数据库的操作
db.session.add(new_user)
#db.session.commit()提交会话中所有待处理的更改并保存到数据库
db.session.commit()

#查询用户
#User.query查询接口，可以执行各种查询操作
#filter_by添加过滤条件 .first()返回第一个记录，若无匹配则返回None
user = User.query.filter_by(username = "JohnDoe").first()
if user:
    print(f"User found:{user.username}")
else:
    print("User not found")
    
#filter允许使用更复杂的条件进行查询
#filter_by以关键字参数形式指定过滤条件，是和简单查询过滤
user2 = User.query.filter(User.username == "JohnDoe").first()

#join进行连接查询  outjoin进行外连接查询
user3 = User.query.join(Post).filter(Post.title == "Flask")
user4 = User.query.outerjoin(Post).all()

#like模糊查询
user5 = User.query.filter(User.username.like("John%")).all()

#更新用户
user.email = "newemail@example.com"
db.session.commit()

#删除用户
db.session.delete(user)
db.session.commit()
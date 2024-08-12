from sqlalchemy import create_engine,Column,Integer,String
#工厂函数，创建一个基类，所有的ORM模型继承此类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#创建数据库连接
engine = create_engine("sqlite:///example.db")

#声明基类
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    username = Column(String,unique = True,nullable = False)
    email = Column(String,unique= True,nullable= False)
    
#创建表
Base.metadata.create_all(engine)

#创建会话类
Session = sessionmaker(bind=engine)#绑定数据库连接
#创建会话实例，所有数据库操作都通过此实例对象来执行
session = Session()

#插入数据
new_user = User(username = "Alice",email = "Alice@example.com")
session.add(new_user)
session.commit()

#查询数据
users = session.query(User).all()
for user in users:
    print(user.username,user.email)
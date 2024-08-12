#适用于对SQL语句有明确需求嗯或者需要使用数据库特定功能的场景
#通过Python代码生成并执行Python语句

from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String

#创建一个数据库连接,
#create_engine创建数据库连接引擎，是SQLAlchemy和数据库交互的接口
engine = create_engine("sqlite:///example.db")

#定义表的元数据
#Meta是保存表结构的元数据，存储表的结构
metadata = MetaData()

#定义一个表
users_table = Table("users",metadata,#定义一个users表，将其与metadata相关联
    Column("id",Integer,primary_key=True),
    Column("username",String,nullable=False),
    Column("email",String,nullable=False)                   
)

#创建表
#前面进行了关联，这里进行建表
metadata.create_all(engine)

#插入数据
with engine.connect() as conn:
    #execute执行
    conn.execute(users_table.insert(),[
        {"username":"alice","email":"alice@example.com"},
        {"username":"bob","email":"bob@example.com"}
    ])
    
    
#查询数据
with engine.connect()as conn:
    #select()函数生成一个select SQL查询返回全表
    result = conn.execute(users_table.select())
    for row in result:
        print(row)
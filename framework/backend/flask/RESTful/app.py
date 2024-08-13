from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#将flask应用与restful api结合起来
api = Api(app)

#连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)

#创建表模型
class Post(db.model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

#设置了一个解析器 解析请求中的数据
#创建RequestParser解析器实例
post_parser = reqparse.RequestParser()
#添加两个预期参数 title和content 请求到达时解析请求参数是否符合预期 不符合则返回错误信息
#确保服务器接收符合预期格式和内容的请求数据 实现健壮性
post_parser.add_argument("title",type=str,required=True,help="Title cannot be blank")
post_parser.add_argument("content",type=str,required=True,help="Content cannot be blank")


#处理单个文章的资源类
#需要post_id参数
class PostResource(Resource):
    #对get,put等方法进行覆写
    def get(self,post_id):
        post = Post.query.get_or_404(post_id)
        return {"id":post.id,"title":post.title,"content":post.content}
    
    def put(self,post_id):
        #parse_args 当请求到达时解析请求中的参数 返回包含所有解析后参数的字典
        args = post_parser.parse_args()
        #从数据库中获取对应id的文章，找不到则返回404错误
        post = Post.query.get_or_404(post_id)
        #对内容进行更新
        post.title = args["title"]
        post.content = args["content"]
        db.session.commit()
        return {"id":post.id,"title":post.title,"content":post.content}
    
    def delete(self,post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete()
        return "",204
    
#处理所有文章的列表查询和新文章的创建操作
#不需要post_id参数
class PostListResourse(Resource):
    def get(self):
        posts = Post.query.all()
        return [{"id":post.id,"title":post.title,"content":post.content} for post in posts]
    
    def post(self):
        args = post_parser.parse_args()
        new_post = Post(title=args["title"],content=args["content"])
        db.session.add(new_post)
        db.session.commit()
        return {"id":new_post.id,"title":new_post.title,"content":new_post.content}
    
#将资源添加到API中  将资源类与特定的URL路径关联
#不同的HTTP请求方法对应资源类的不同方法  默认是get方法
api.add_resource(PostResource,"/posts/<int:post_id>")
api.add_resource(PostListResourse,"posts")

if __name__ == "__main__":
    app.run(debug=True)
#Flask-RESTful api封装Flask的路由系统。简化RESTful API的构建

from flask import Flask,jsonify,request
from flask_restful import Api,Resource

#API文档的自动生成
from flasgger import Swagger

app = Flask(__name__)
#将Flask应用同RESTful api结合起来
#api是一个Api实例
api = Api(app)

#自动生成api文档
swagger = Swagger(app)

#定义一个资源类
class HelloWorld(Resource):
    def get(self):
        return {"message":"Hello, world"}
    
#处理json数据
@app.route("/json")
def get_json():
    data = {"name":"Alice","age":30}
    return jsonify(data)

#将资源添加到API中
#指定URL端点为"/" 当访问根路径"/"时资源get方法被调用
#flask-restful会自动调用相应的资源方法将返回值转化为JSON响应 并自动设置响应头
api.add_resource(HelloWorld,"/")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,Response,render_template

#创建Flask应用
#使用name来确定应用的根路径
app = Flask(__name__)

#定义路由和视图函数
#路由注册
@app.route("/")
def hello():
    return("Hello, Flask")

@app.route("user/<name>")
def user(name):
    return f"Hello, {name}!"

#请求钩子，共四种，允许开发者在不同的阶段插入自定义逻辑
#after_request teradown_request before_request before_first_request
@app.before_request
def before_request_func():
    print("before requset")

#flask如果返回字符串，会自动封装成一个Response对象
#开发者也可以自定义Response对象
@app.route("/custon")
def custom_response():
    return Response("Custom Response",status=200,mimetype="text/plain")

#使用Jinja2模板渲染
@app.route("/hello/<name>")
def hello(name):
    #flask会找到templates/hello.html并将name变量的值插入到指定位置
    return render_template("hello.html",name = name)


#name表示当前模块的名字
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,jsonify, render_template

app = Flask(__name__)

#全局错误处理器 捕获所有未处理异常
@app.errorhandler(Exception)
def handle_exception(e):
    response  = {
        "error":"An unexpected errot occurred.",
        "message":str()
    }
    return jsonify(response),500

#前后端分离式 返回错误信息给前端处理

#处理404即请求资源未找到 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error ="Page not found"),404

#处理错误请求 返回错误信息给前端处理
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad request"),400

#自定义异常
class CustomError(Exception):
    pass

#定义路由抛出异常
@app.route("/custom")
def custom_error():
    raise CustomError("This is a custom error")

#处理自定义异常  返回JSON响应 包含错误信息
@app.errorhandler(CustomError)
def handle_custom_error(e):
    return jsonify(error=str(e)),400

#返回HTML界面适合传统Web 非前后端分离

#实现自定义错误界面
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"),500

#自定义实现除零异常
@app.route("divide")
def divide():
    num = 10
    divisor = 0 
    result = num/divisor
    return jsonify(result=result)

#捕捉异常并返回错误消息而不是让程序崩溃
@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(e):
    return jsonify(error="Division by zero is not allowed"),400
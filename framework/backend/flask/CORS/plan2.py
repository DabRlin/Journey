from flask import Flask, request, jsonify

app = Flask(__name__)

#手动设置响应头部中的CORS头部实现跨域访问
@app.after_request
def after_request(response):
    #指定允许访问的资源来源
    response.headers.add("Access-Control-Allow-Origin","*")
    #列出允许的自定义响应头
    response.headers.add("Access-Control-Allow-Headers","Content-Tyoe,Authorization")
    #列出允许的HTTP方法
    response.headers.add("Access-Control-Allow-Methods","GET,POST,PUT,DELETE,OPTIONS")
    return response
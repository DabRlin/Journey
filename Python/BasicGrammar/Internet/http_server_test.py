#创建一个简单的http服务器

# impleHTTPRequestHandler：这是一个处理 HTTP 请求的简单请求处理器
# 通常用于开发和测试。它能够处理 GET 和 HEAD 请求，并自动提供当前目录的文件。
# HTTPServer：这是一个简单的 HTTP 服务器类，用于监听和处理 HTTP 请求
from http.server import SimpleHTTPRequestHandler,HTTPServer

#设置服务器接口
PORT = 8080

#指定了请求处理器类，将用SimpleHTTPRequestHandler处理所有进入的HTTP请求
handler = SimpleHTTPRequestHandler

#创建了一个HTTPserver服务器实例
httpd = HTTPServer(("localhost",PORT),handler)

#启动服务器
print(f"Serving on port {PORT}")
#启动服务器进入无限循环，处理HTTP请求
httpd.serve_forever()
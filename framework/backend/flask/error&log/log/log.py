import logging
#处理日志文件的滚动
from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask(__name__)

#判断是否在调试状态下运行 不在调试状态下运行才配置记录日志
if not app.debug:
    #记录到文件
    #设置日志文件的名称，日志文件的最大字节数为10KB,最多保留个数为10个
    file_handler = RotatingFileHandler("app.log",maxBytes=10240,backupCount=10)
    #只有INFO级别及以上的日志才会被记录
    file_handler.setLevel(logging.INFO)
    #设置日志格式 时间 - 日志级别 - 日志信息
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s -%(message)s'))
    #将配置好的文件日志处理器添加到Flask应用的日志记录器中
    app.logger.addHandler(file_handler)
    
    #记录到控制台
    #创建一个控制台日志文件 将日志输出到控制台 开发人员测试使用
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s -%(message)s'))
    #将配置好的控制台日志处理器添加到Flask应用的日志记录器中
    app.logger.addHandler(console_handler)
    
@app.route("/log_example")
def log_example():
    #记录三种级别的日志
    app.logger.info("This is an info message")
    app.logger.warning("This is a warning message")
    app.logger.error("This is an error message")
    #返回字符串作为显示页面内容
    return "Logging example"
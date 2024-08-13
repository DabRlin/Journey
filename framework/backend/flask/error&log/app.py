from flask import Flask,render_template,jsonify
import logging
from logging.handlers import RotatingFileHandler

#创建应用
app = Flask(__name__)

#配置日志记录
if not app.debug:
    file_handler = RotatingFileHandler("app.log",maxBytes=10240,backupCount=10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(file_handler)
    
@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f"404 error:{e}")
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_error(e):
    app.logger.error(f"500 error:{e}")
    return render_template("500.html"),500

#引发一个错误 这里是服务端逻辑错误会被500捕捉
@app.route("/error")
def error_route():
    return 1/0

if __name__ == ("__main__"):
    app.run(debug=False)
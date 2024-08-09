import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse,parse_qs

def query_student(student_id):
    conn = sqlite3.connect("Demo/demo3/students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?",(student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #定义私有方法，设置请求头
    def _set_headers(self,status_code = 200,content_type ="application/json"):
        self.send_response(status_code)
        self.send_header("Content-Type",content_type)
        self.send_header("Access-Control-Allow-Origin","*")
        #表示头部信息设置完成
        self.end_headers()
        
    #BaseHTTPRequestHandler中的一个方法
    #处理GET请求时，会调用这个方法
    def do_GET(self):
        #解析URL路径
        parsed_path = urlparse(self.path)
        if parsed_path == "/get_student":
            #解析
            query_params = parse_qs(parsed_path.query)
            student_id = query_params.get("id",[None])[0]
            if student_id:
                student = query_student(student_id)
                if student:
                    response = {
                        "id" :student[0],
                        "name" :student[1],
                        "gender" :student[2],
                        "major" : student[3]
                    }
                    self._set_headers()
                else:
                    response = {"error":"Student not found"}
                    self._set_headers(404)
            else:
                response = {"error":"Missing student id"}
                self._set_headers(400)
        else:
            response = {"error":"Invalid endpoint"}
            self._set_headers(404)
        #wfile是写入输出流的对象，通常用于发送响应数据给客户端
        self.wfile.write(json.dumps(response).encode("utf-8"))
        
def run(server_class = HTTPServer,handler_class = SimpleHTTPRequestHandler, port = 5000):
    server_address = ("localhost",port)
    #指定请求器类，将调用SimpleHTTPRequestHandler来处理所有进入的HTTP请求
    #httpd 是http deamon的缩写，deamon是一种在后台运行的计算机程序，常用于处理网络请求或执行系统任务
    httpd = server_class(server_address,handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()
    
if __name__ =="__main__":
    run()
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

def query_student(student_id):
    conn = sqlite3.connect('Demo/demo3/students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/get_student':
            query_params = parse_qs(parsed_path.query)
            student_id = query_params.get('id', [None])[0]
            if student_id:
                student = query_student(student_id)
                if student:
                    response = {
                        'id': student[0],
                        'name': student[1],
                        'gender': student[2],
                        'major': student[3]
                    }
                else:
                    response = {'error': 'Student not found'}
                    self._set_headers(404)
            else:
                response = {'error': 'Missing student id'}
                self._set_headers(400)
        else:
            response = {'error': 'Invalid endpoint'}
            self._set_headers(404)
        
        self._set_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=5000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
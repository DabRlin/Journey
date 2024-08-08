from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # 解决跨域问题

def query_student(student_id):
    conn = sqlite3.connect('Demo/demo2/students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

@app.route('/get_student', methods=['GET'])
def get_student():
    student_id = request.args.get('id')
    student = query_student(student_id)
    if student:
        return jsonify({
            'id': student[0],
            'name': student[1],
            'gender': student[2],
            'major': student[3]
        })
    else:
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)

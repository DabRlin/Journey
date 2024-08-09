from flask import Flask,request,jsonify,render_template
import sqlite3

app = Flask(__name__)

#链接数据库并返回数据
def query_student(student_id):
    conn = sqlite3.connect("Demo/demo1/students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?",(student_id))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student

@app.route("/")
def index():
    return render_template("index.html")

@app.route("get_student",method = ["GET"])
def get_student():
    #通过url获取id参数
    student_id = request.args.get("id")
    student = query_student(student_id)
    if student:
        return jsonify({
            "id":student[0],
            "name":student[1],
            "gender":student[2],
            "major":student[3]
    })
    else:
        return jsonify({"error":"student not found"}),404
    
if __name__ == "__main__":
    app.run(debug=True)
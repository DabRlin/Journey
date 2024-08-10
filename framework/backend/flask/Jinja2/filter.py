from flask import Flask,render_template

app = Flask(__name__)

#定义一个自定义过滤器，将字符串反转
@app.template_filter("reverse")
def reverse_string(s):
    return s[::-1]

@app.route("/")
def index():
    example_text = "Hello world!"
    return render_template("test.html",text = example_text)

if __name__== "__main__":
    app.run(debug=True)
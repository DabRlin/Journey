from flask import Flask,render_template,flash,redirect,url_for,jsonify
from forms import RegistrationForm,LoginForm
from flask_wtf import CSRFProtect,csrf_exempt

app = Flask(__name__)
#设置用于生成CSRF令牌的密钥
app.config["SECRET_KEY"]="your_serect_key_here"
#启用CSRF保护
csrf = CSRFProtect(app)

@app.route("/register",method = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.date}!","success")
        #url_for函数通过函数名生成对应的url
        return redirect(url_for("home"))
    #表单验证失败（返回界面显示错误）或者GET请求（返回CSRF令牌）
    return render_template("register.html",form = form)

@app.route("/home")
def home():
    return "Welcome to the Home Page!"

@app.route("/login",method = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login successful","success")
        return redirect(url_for("home"))
    return render_template("login.html",form = form)

#启用保护就要注意发送请求时要包含CSRF令牌
@app.route("/api/data")
#禁用此路由的CSRF保护
@csrf_exempt
def api_data():
    return jsonify(success = True)

if __name__ == "__main__":
    app.run(debug=True)
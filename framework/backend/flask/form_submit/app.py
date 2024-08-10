from flask import Flask, request,render_template,flash,redirect,url_for
from forms import RegistrationForm

app = Flask(__name__)
#设置令牌进行CSRF保护
app.config["SECRET_KEY"]="your_secret_key_here"

@app.route("/submit",method = {"GET","POST"})
def sumbit():
    #处理post请求
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"Username:{username}, Password:{password}"
    #处理get请求
    return "Submit the form!"
    
    
@app.route("register",method=["GET","POST"])
def register():
    #实例化自定义表单对象
    #Flask-WTF会自动将数据填充到form对象中
    form = RegistrationForm()
    #验证表单数据是否符合验证
    if form.validate_on_submit():
        #显示登录成功，跳转到home界面
        flash(f"Accoutn created for {form.username.data}!","success")
        return redirect(url_for("home"))
    #如果表单未通过验证或者是一个get请求
    return render_template("register.html",form=form)

@app.route("/home")
def home():
    return "Welcome to the home page!"
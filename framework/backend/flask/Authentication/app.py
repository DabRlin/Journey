from flask import Flask, redirect, render_template, request, url_for,abort
from flask_sqlalchemy import SQLAlchemy
#导入包生成密码哈希值和验证密码哈希值
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, login_required,login_user,logout_user,LoginManager,current_user

#创建应用
app = Flask(__name__)
#连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
db = SQLAlchemy(app)


#处理用户登录
login_manager = LoginManager()
login_manager.init_app(app)

#用户加载函数 登陆后将用户返回到current_user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#定义重定向登录界面，用户未登录访问受保护界面时跳转
login_manager.login_view = "login"

#设置未认证用户访问受保护界面时显示的消息
login_manager.login_message = "Please log in to access this page."
#设置消息类别
login_manager.login_message_category = "info"


#建立关系对照模型
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nulable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password_hash =db.Column(db.String(128),nullable = False)
    #active = db.Column(db.boolean,default=True)
    
    #设置哈希值密码
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        
    #检查密码哈希值是否匹配
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    #基于角色访问控制权限
    def is_admin(self):
        return self.role == "admin"
    
    #覆写is_active方法
    #def is_active(self):
        # return self.active
    

#定义路由
#用户注册
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        #创建用户实例
        user = User(username=username,email=email)
        #设置密码哈希值
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

#登录用户
@app.route("/login",method = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            #登录用户，选择不记住我
            login_user(user,remember=False)
            return redirect(url_for("dashboard"))
        return render_template("login.html")
    
#注销登录
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

#定义管理员界面
@app.route("/admin")
def admin_dashboard():
    if not current_user.is_authenticated or not current_user.is_admin():
        abort(403)
    return render_template("admin_dashbord.html")

#定义主界面
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


#定义保护访问界面
@app.route("/protected")
@login_required
def protected():
    return f"Hello, {current_user.username}"

if __name__ == "__main__":
    app.run()
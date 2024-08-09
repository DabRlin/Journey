from flask import Flask,redirect,request

#创建应用
app = Flask(__name__)

#定义路由
#flask通过装饰器来定义路由
@app.route("/some/url")
def some_function():
    return "response"        

#url路径中的变量
@app.route("/user/<username")
def show_user_profile(username):
    return f"user:{username}"

#url变量指定类型
@app.route("/post/<int:post_id")
def show_post(post_id):
    return f"Post ID:{post_id}"

#创建多个视图函数处理不同请求
@app.route("/")
def home():
    return "Welcome to the homepage"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "This is the contact page"


#多个规则对应同一个视图函数
@app.route("/login")
@app.route("/signin")
def login():
    return "This is the login page"

#设置method参数
@app.route("/submit",method = ["GET","POST"])
def submit():
    if request.method == "POST":
        return "Form submitted"
    else:
        return "Please sumbit the form"
    
#URL重定向
@app.route("/old-url")
def old_url():
    #通过redirect重定向到new-url
    return redirect("/new-url")

@app.route("/new-url")
def new_url():
    return "This is new url"

#路由的优先级，flask路由是按顺序匹配的
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User:{username}"

@app.route("/user/admin")
def admin():
    return "Hello admin"

# 这里 /user/admin 会被认为是一个 username，
# 因为 /user/<username> 路由先定义。
# 因此，需要将 /user/admin 路由放在前面，确保它能被正确匹配

#<path:subpath>允许subpath包含路径
@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"subpath:{subpath}"

#多个变量
@app.route("/user/<username>/post/<int:post_id>")
def show_user_post(username,post_id):
    return f"User:{username},PostId:{post_id}"

#默认值和可选参数
#用户访问page/时，page_num的值为默认值1
#用户访问page/2时，page_num的值为2
@app.route("/page/<int:page_num")
@app.route("/page/",defaluts={"page_num":1})
def show_page(page_num):
    return f"Page number:{page_num}"
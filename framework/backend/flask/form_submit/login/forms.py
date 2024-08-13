from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email

#使用Flask-WTF进行表单处理时，会自动成一个令牌，令牌会随着表单数据一起提交

#自定义注册表单对象
class RegistrationForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(),Length(min=4,max=25)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = StringField("Password",validators=[DataRequired(),Length(min=4,max=25)])
    submit = SubmitField("Sign up")
    
#自定义登录表单对象
class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
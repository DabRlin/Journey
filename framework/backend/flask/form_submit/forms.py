from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,Email,ValidationError

#定义表单类
class RegistrationFrom(FlaskForm):
    #将表单中的类定义为类的属性，每一个字段都是WTForms提供的一个字段类
    #通过validators来进行表单验证
    username = StringField("Username",validators=[DataRequired(),Length(min=4,max=25)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("password",validators=[DataRequired(),Length(min=6)])
    #与HTML表单相对应
    submit = SubmitField("Sign Up")
    
#自定义验证器
#当用户提交表时，Flask-WTF会自动调用与字段关联的所有验证器
    def validate_username(self,username):
        #通过ORM如SQLAlchemy进行用户查询
        user = User.query.fliter_by(username = username.data).first()
        #如果用户已经存在，返回异常并显示错误消息
        if user:
            raise ValidationError("This username is already taken. Please choose a different one")
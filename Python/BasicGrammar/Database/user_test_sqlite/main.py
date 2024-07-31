from user_sqlite import User

#创建新用户
new_user = User(name = "Bob", age = 28, email="Bob@qq.com")
new_user.save()

#获取用户
user = User.get_by_id(22)
print(user)

#更新用户
if user:
    user.name = "Alice Updated"
    user.save()
    
#获取所有用户
users = User.get_all()
print(users)

#删除用户
User.delete_by_id(22)
users = User.get_all()
print(users)
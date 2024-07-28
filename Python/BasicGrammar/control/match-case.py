#选择控制语句

#创建控制流函数
def handle_status(status):
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case _:
            print("Unkonwn status")
        
handle_status(200)
handle_status(404)
handle_status(2000)
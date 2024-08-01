import socket

#TCP客户端
#创建一个TCP套接字
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接到服务器
client_socket.connect(('localhost',12345))

#发送数据
client_socket.sendall(b"Hello, server")

#接收数据
response = client_socket.recv(1024)
print("Recived",response.decode())

#关闭连接
client_socket.close()

#TCP服务器
#创建一个TCP套接字
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定到地址和端口
server_socket.bind('localhost',12345)

#监听连接
server_socket.listen(1)
print('Server is listening...')

#接收连接
conn,addr = server_socket.accept()
print("Connected by",addr)

#接收最多1024数据
data = conn.recv(1024)
print("Received",data.decode())

#发送数据到客户端
conn.sendall(b"Hello,client")

#关闭连接
conn.close()
server_socket.close()

# 角色和功能：
# TCP客户端：
# 发起连接请求。
# 发送数据请求和接收服务器响应。
# TCP服务器：
# 等待和接受客户端的连接请求。
# 接收客户端数据并提供响应。

# 连接过程：
# TCP客户端：
# 主动调用 connect() 方法连接到服务器。
# TCP服务器：
# 被动调用 bind() 方法绑定到特定地址和端口，调用 listen() 方法监听连接请求，然后使用 accept() 方法接受连接。

# 通信发起者：
# TCP客户端：
# 通常是通信的发起者，首先发送数据或请求。
# TCP服务器：
# 通常是通信的响应者，等待并处理客户端请求。
#用于底层网络通信

import socket

#创建一个TCP/IP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接到服务器
server_address = ('localhost',8080)
sock.connect(server_address)

#发送数据
message = "Hello, Web!"
#将消息编码为字节并通过socket发送到服务器，sendall确保消息完全发送
sock.sendall(message.encode())

#接收数据
data = sock.recv(1024)
print("Received",data.decode())

#关闭连接
sock.close()
#用于编写异步I/O操作的库，适用于高并发网络编程
import asyncio

#定义异步函数
#创建异步TCP客户端
async def tcp_client():
    #await关键字等待asyncio.open_connection完成
    #建立到指定端口的TCP连接，返回StreamReader对象和StreamWriter对象
    reader,writer = await asyncio.open_connection('localhost',12345)
    
    #发送数据，传输字节流故使用b
    writer.write(b'Hello, server')
    #异步操作，知道数据发送完成
    await writer.drain()
    
    #从服务器读取最多一千字节的数据，await实现异步
    data = await reader.read(1000)
    #decode解码为字符串
    print(f"Received:{data.decode()}")
    
    #关闭写入流
    writer.close()
    #异步等待写入流完全关闭
    await writer.wait_closed()
    
#运行异步函数asyncio.run是一个高级API用于运行一个顶层的异步函数
#用于管理循环事件的创建和销毁
asyncio.run(tcp_client())

#创建异步TCP服务器
async def handle_client(reader,writer):
    data = await reader.read(100)
    message = data.decode()
    #获取客户端地址信息
    addr = writer.get_extra_info('peername')
    #打印接收到的消息及来源地址
    print(f"Received {message!r} from {addr!r}")
    
    #打印即将发送的消息
    print(f"Send: Hello, client")
    #向客户端发送响应消息
    writer.write(b"Hello,client")
    
    #等待直到数据发送完成
    await writer.drain()
    
    #关闭写入流
    writer.close()
    await writer.wait_closed()
    
    #定义异步函数main用于启动服务器
async def main():
    #启动服务器
    server = await asyncio.start_server(handle_client,'localhost',12345)
    #获取服务器地址
    addr = server.sockets[0].getsockname()
    #打印正在监听的服务器地址
    print(f"Serving on {addr}")
    
    #使用异步上下文管理服务器的生命周期
    async with server:
        #运行服务器并处理客户端连接直到服务器被关闭
        await server.serve_forever()
    
asyncio.run(main())
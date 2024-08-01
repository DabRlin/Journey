#用于处理WebSocket协议的库
import asyncio
import websockets

#WebSocket服务器
# websocket：WebSocket 连接对象，用于发送和接收消息。
# path：请求的路径
async def echo(websocket,path):
    #async for异步循环
    async for message in websocket:
        #将接收到的消息原样返回客户端，实现"回音"
        await websocket.send(message)
    
#创建了一个websocket服务器,绑定到localhost和端口8765，echo是处理器函数
start_server = websockets.serve(echo,'localhost',8765)

#在时间循环中运行WebSocket服务器，直到服务器启动
#event loop 事件循环
asyncio.get_event_loop().run_until_complete(start_server)
#使事件循环运行，保持服务器运行状态
asyncio.get_event_loop().run_forever()

#websocket客户端
async def hello():
    url = "ws:/localhost:8765"
    #async with异步上下文管理，与传统with类似，这里用于异步
    async with websockets.connect(url) as websocket:
        #发送消息
        await websocket.send("Hello, World")
        #接收响应消息
        response = await websocket.recv()
        #打印响应消息
        print(f"Recived:{response}")

#循环运行客户端直到客户端操作完成
asyncio.get_event_loop().run_until_complete(hello())

# 异步编程
# 异步编程是指在程序中允许某些操作在等待完成的同时执行其他任务。它是为了提高程序的效率，尤其是在处理 I/O 密集型操作时。传统的同步编程在等待 I/O 操作完成时会阻塞其他操作，而异步编程允许程序在等待时继续执行其他任务。

# 协程（Coroutine）
# 协程是异步编程中的一种特殊函数，它可以挂起执行，并在之后恢复执行。这使得程序可以在等待 I/O 操作时运行其他任务。协程使用 async 关键字定义，并且可以使用 await 关键字来挂起执行直到某个异步操作完成。

# 循环与协程的关系
# 协程和异步编程都涉及到事件循环（event loop）。事件循环是一个机制，它负责调度协程的执行，处理异步任务，并管理程序的异步操作。

# 事件循环（Event Loop）
# 事件循环是协程和异步编程的核心组件。它不断运行，监控各种 I/O 操作和任务的状态，并在任务准备好时继续执行它们

# 异步编程的实现：

# 使用 async 和 await 关键字定义和调用协程。
# 使用 asyncio 提供的事件循环来调度协程的执行。
# 协程的实现：

# 协程可以被挂起和恢复执行。这使得协程可以在执行异步操作时释放控制权，并在操作完成后恢复执行。
# 协程的执行需要依赖事件循环来管理。
# 事件循环的实现：

# 事件循环负责管理协程的执行。它会监控 I/O 操作，并在 I/O 操作完成后恢复挂起的协程。
# 在 Python 中，asyncio 的 get_event_loop() 方法可以获取事件循环，asyncio.run() 可以启动事件循环并运行协程。
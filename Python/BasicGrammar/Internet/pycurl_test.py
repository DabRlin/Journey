#提供cURL的Python接口，适用于复杂的HTTP请求

import pycurl

from io import BytesIO

#创建内存缓冲区，存储HTTP响应数据
buffer = BytesIO()
#配置cURL对象
c = pycurl.Curl()
#设置URL
c.setopt(c.URL,"http://example.com")
#设置选项：将响应数据写入到buffer中
c.setopt(c.WRITTEDATA,buffer)
#perfo执行配置好的cURL请求
c.perform()
c.close()

#获取并打印响应数据，返回内存缓冲区中的所有内容
body = buffer.getvalue()
print(body.decode('utf-8'))
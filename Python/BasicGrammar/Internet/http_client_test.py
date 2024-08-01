#用于处理HTTP请求

import http.client

# 使用 HTTPS 连接
conn = http.client.HTTPSConnection('chatgpt.com')

#发送HTTP请求
conn.request("GET", "/")
#获取和处理响应
response = conn.getresponse()

#打印响应内容
print(response.status, response.reason)
data = response.read()
print(data.decode())

#关闭连接
conn.close()
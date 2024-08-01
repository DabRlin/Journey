#用于发送HTTP请求

import requests
url = "https://chatgpt.com"

#发送get请求，response存储服务器的响应
response = requests.get(url)

#打印信息
print(response.status_code,response.reason)
print(response.text)

#定义一个包好数据的字典作为POST的请求体
data ={"key":"value"}

#发送post请求到url，将data作为json数据发送
response = requests.post(url,json = data)
print(response.status_code)
print(response.json())
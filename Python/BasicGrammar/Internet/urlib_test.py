#用于处理URL

from urllib import request,parse

#发送get请求并读取响应
response = request.urlopen("https://jsonplaceholder.typicode.com/posts/1")
#读取数据并打印
data = response.read()
print(data.decode('utf-8'))

#发送post请求
url = "https://jsonplaceholder.typicode.com/posts"
#将字典数据编码为url编码的查询字符串格式
data = parse.urlencode({"key":"value"})
#构造请求对象
req = request.Request(url,data=data,method='POST')
#发送post请求并读取响应
response = request.urlopen(req)
print(response.read().decode("utf-8"))
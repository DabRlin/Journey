# 不可变 (Immutable)：一旦创建，元组的内容不能更改。
# 支持索引和切片：类似于字符串和列表，可以通过索引访问元素，使用切片访问子元组。
# 可以包含不同类型的元素：一个元组可以包含不同类型的数据。
# 适合存储不需要改变的数据：由于不可变性，元组适合存储常量数据。

#创建元组
t = (1,2,2,4)

#计数返回元素个数
print(t.count(2))
print(t[1])

#返回元素索引
print(t.index(2))
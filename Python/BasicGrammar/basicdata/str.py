# 不可变 (Immutable)：一旦创建，字符串的内容不能更改。
# 支持索引和切片：可以通过索引访问单个字符，使用切片访问子字符串。
# 支持多种操作：包括拼接 (+)，重复 (*)，查找 (find, index)，替换 (replace)，拆分 (split)，以及许多其他方法。

#创建字符串
s = " Hello world! "

#全部小写
print(s.lower())

#全部大写
print(s.upper())

#首字母大写
print(s.capitalize())

#移除字符串开头和结尾的空格
print(s.strip())

#替换字符串
print(s.replace("world", "Python"))

#将字符串按照指定分隔符拆分成列表
print(s.split(" "))
words = ["Hello","world!"]

#将列表的元素按指定分隔符分割拼接成字符串
print(" ".join(words))

#查找子字符串，返回第一个匹配的索引
print(s.find("He"))
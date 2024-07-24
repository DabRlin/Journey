# 键值对存储 (Key-Value Pairs)：数据以键值对的形式存储，每个键是唯一的。
# 无序 (Unordered)：Python 3.7 之前，字典中的键值对没有特定的顺序。从 Python 3.7 开始，字典保持插入顺序。
# 可变 (Mutable)：可以动态增加、删除或修改键值对。
# 高效查找：通过键查找值非常高效。

#创建字典
d = {"name":"alice","age": 15}

#返回所有键和所有值
print(d.keys())
print(d.values())

#返回所有的键值对
print(d.items())

#根据键返回值
print(d.get("name"))
#找不到时默认返回
print(d.get("gender"),"unknown")

#用另一个字典或者键值对更新当前字典
d.update({"age":25,"gender":"Female"})
print(d)

#弹出指定键的值
age = d.pop("age")
print(age)
print(d)

#移除并返回字典中最后一个键值对
item = d.popitem
print(item)
print(d)

#清空字典
d.clear()
print(d)
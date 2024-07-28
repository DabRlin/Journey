# 无序 (Unordered)：集合中的元素没有特定的顺序。
# 唯一 (Unique)：集合中的每个元素都是唯一的，重复的元素会被自动去重。
# 可变 (Mutable)：可以动态增加或删除元素。
# 支持集合操作：如并集、交集、差集等。

#集合的创建
s = {1,2,3,4}

#元素添加
s.add(5)
print(s)

#元素移除,元素不存在会报错
s.remove(2)
print(s)

#元素移除，元素不存在不会报错
s.discard(5)
print(s)

#弹出随机元素
print(s.pop())

#清空集合
s.clear()
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

#返回集合的并集
print(s1.union(s2))

#返回集合的交集
print(s1.intersection(s2))

#返回集合的差集
print(s1.difference(s2))
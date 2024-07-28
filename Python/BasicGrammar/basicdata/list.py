# 可变 (Mutable)：可以动态增加、删除或修改元素。
# 支持索引和切片：可以通过索引访问元素，使用切片访问子列表。
# 可以包含不同类型的元素：一个列表可以包含不同类型的数据。
# 常用的数据结构：由于其灵活性，列表在 Python 中非常常用。


#创建列表list
numbers = [1,2,3]
print(numbers)
print(numbers[1])
#添加元素
numbers.append(4)
print(numbers)

#拓展列表
numbers.extend([8,9])
print(numbers)

#在指定位置插入元素
numbers.insert(1,1.3)
print(numbers)

#移除指定位置元素
numbers.remove(1)
print(numbers)

#弹出指定位置元素
print(numbers.pop(3))
print(numbers)
numbers = [1,2,3]

#查指定元素的索引
print(numbers.index(2))
numbers = [1,2,2,4]

#计数
print(numbers.count(2))
numbers = [2,1,4,5,4,2,1]

#排序
numbers.sort()
print(numbers)
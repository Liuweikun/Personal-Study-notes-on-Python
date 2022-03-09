print("集合")
#集合是无序可变，元素不能重复，实际上，集合的底层是字典实现的，
#集合的所有元素都是字典的键对象，因此是不能重复且唯一的

print("集合的创建与删除")
a = {10,20,30,"chenyanyu"}
a.add(20)
print(a)

#set()函数，将列表，元组等可迭代对象转化成集合，如果数据存在重复数据，则只保留一个

a = ['a','b','c']
b = set(a)
print(b)

a = {10,20,30,40,50}
a.remove(20)  #删除指定元素
print(a)

a.clear()    #将集合中所有内容清空
print(a)


print("集合中的操作")
#与数学概念相同，集合中也存在并集，交集，差集等运算
a = {1,3,"chenyanyu"}
b = {2,4,3,"lover"}
print("并集")    #两集合所有元素相加,有两种表达方式
print(a|b)
print(a.union(b))
print("交集")    #两集合重合的元素，两种表达方式
print(a&b)
print(a.intersection(b))
print("差集")
print(a-b)     #以减号前面的集合为主体，减去后面集合里相同的元素，两种表达方式
print(b-a)
print(a.difference(b))
print(b.difference(a))
  







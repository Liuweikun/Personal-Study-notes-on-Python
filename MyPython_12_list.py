print("序列")
#什么叫序列，序列是一种数据存储方式，用来存放一系列的数据
#在内存中，序列就是一块用来存放多个值的连续的内存空间
#字符串，列表，元组，字典，集合都属于常见的序列结构


print("列表")
#列表是内置可变序列，是包含多个元素的有序连续的内存空间，列表中的元素可以各不相同，可以是任意类型

a = [10,20,30,40]
print(id(a))
print(id(a[0]))     #python一切皆对象，所以列表和单个元素都有对应的对象id
print(id(a[1]))     #python一切皆对象，所以列表和单个元素都有对应的对象id
print(id(a[2]))     #python一切皆对象，所以列表和单个元素都有对应的对象id
print(id(a[3]))     #python一切皆对象，所以列表和单个元素都有对应的对象id
print(a[0])         #通过索引来确定元素的位置

b = [10,20,'abc',True]
print(b)               #列表可以是各种数据类型

print("[]基本语法创建列表")

a = []                  #空
b = [10,20,'abc',True]   #可以存储任何类型的数据
print(id(a))             #列表可以往里面增加元素，且不会新建对象
a.append(20)
print(a)
print(id(a))

print("list()创建列表")
#list()目的是将其他任何可迭代的数据转化成列表，比如字符串，比如range等等

c = list()    # 通过list()创建了一个空列表c
print(c)

c = list(range(10))
print(c)      #将range(10)分割，转化成了列表c里面的元素

c = list("baixiaochun,jiayou")
print(c)     #也可以将字符串转化成为列表c当中的元素


print("range()创建整数列表")
 #range()可以帮我们非常方便的创建整数列表，很常用
 #格式：range(start,end,step),其中start和step可以不写，默认为0和1，但是end必须写，表示结尾数字

a = list(range(5))
b = list(range(0,5,1))
print(a is b)   #虽然内容相同，但不是同一个列表

print(list(range(1,1024,2)))  #这是有步长的列表

print(list(range(1023,0,-2)))  #从后往前，则需要step为负数

print(list(range(-10,-30,-1)))  #当然也可以均为负数

print(list(range(-30,-10,1)))

a = [x*2 for x in range(100) if x%9 == 0]  #意思是遍历0到100所有的整数，且均✖️2，再筛选能被9整除，也就是取余为零的数
print(a)




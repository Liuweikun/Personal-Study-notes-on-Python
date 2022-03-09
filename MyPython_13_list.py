print("列表元素的增加与删除")
#我们一般只在列表的尾部添加元素和删除元素
 
print("\nappend()方法")
a = [20,40]
print(id(a))

a.append([100,200])  #在列表真正的尾部增加元素，速度最快，推荐使用
print(a)
print(id(a))
print(len(a))

print("\n+运算符操作")
b = [30,50]
print(id(b))

b = b + [70]
print(b)        #表面上列表添加了新的元素，实质上是创建了新的列表对象，将原列表的元素和新列表的元素复制到新的列表中，不推荐使用
print(id(b))

print("\nextend()方法")

c = [20,40]
print(id(c))

c.extend([100,200])
print(c)
print(id(c)) 
print(len(c))  #将目标列表中所有的元素都添加到本列表中，属于原地操作，不创建新的列表，与append的区别是：extend是只能接收列表，且将列表中的每个元素
#都添加到原列表中，而append可以接收人意类型的的参数，并不做拆分处理，只是简单的追加到list尾部

print("\n insert插入元素")
d = [10,20,30]
print(d)
print(id(d))

d.insert(2,100)
print(d)        #将指定元素插入到列表对象的任意指定位置，但是会让列表中其他元素发生改变，虽然不涉及创建新的对象，但是依旧不推荐使用，类似的函数还有remove，pop，del
print(id(d))

print("\n乘法扩展")
e = [20,30]
print(id(e))
print(e)

e = e*3
print(id(e))     #用乘法将原列表元素多次重复，从而生成一个新的列表，支持乘法的还有字符串，元组
print(e)

print("列表元素的删除")
a = [10,20,30]
print(id(a))
del a[1]
print("a")
print(id(a))   #是在原有列表内进行的删除操作，删除列表指定位置的元素

a = [10,20,30,40,50]
b = a.pop()
print(b)      #删除并返回指定位置元素，如果未指定位置则默认操作列表最后一个元素
print(a)
c = a.pop(2)
print(c)
print(a)
  
a = [10,20,30,40,50,60,50,40,30,20,10]
print(id(a))
a.remove(20)            #删除首次出现的指定元素，若不存在该元素则抛出异常
#a.remove(80)           抛出异常
print(a)
print(id(a))

print("列表元素的访问与计数")
a = [10,20,30,40,50,60,50,40,30,20,10]
print(a[2])   #通过列表索引访问元素，索引的区间在【0，n-1】这个范围，超出这个范围则会抛出异常

a = [10,20,30,40,50,60,50,40,30,20,10]
print(a.index(20))    #可以获取指定元素首次出现的索引位置，index(value,[start,[end]])
print(a.index(20,2))  #若是指定范围内没有元素，则抛出异常

a = [10,20,30,40,50,60,50,40,30,20,10]
print(a.count(20))      #获得指定元素在列表中出现的次数

a = [10,20,30,40,50,60,50,40,30,20,10]
print(len(a))        #返回列表长度，即列表中包含元素的个数

a = [10,20,30,40,50,60,50,40,30,20,10]
print(10 in a)
print(100 in a)                   #成员资格判断，判断列表中是否存在指定的元素
print(100 not in a )
print(a.count(10)>0)
print(a.count(16)>0)         #也可以通过count来判断是否存在


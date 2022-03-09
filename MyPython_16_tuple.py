print("元组")   #相对于列表的可变序列，元组属于不可变序列，不能修改元组中的元素
a = (10,20,30)
print(type(a))
b = 10,20,30
print(type(b))
c = "10,20,30"
print(type(c))
d = [10,20,30]
print(type(d))
h = {10,20,30}
print(type(h))
e = (20,)
print(type(e))
f = (20)
print(type(f))

a = tuple()
a = tuple("a,b,c")  #将其他序列转成元组  
print(a)
a = tuple(range(3))
print(a)
a = tuple([2,3,4])
print(a)

del a             #元组的删除 

print("元组元素的访问")
ab = (20,30,10,9,8)
print(ab[1])
print(ab[1:3])   #元组元素的访问与列表的访问规则没什么区别
print(ab[:4]) 

b = (20,80,90,10,40)
print(sorted(b))      #元组通过sorted排序后，生成是一个列表

c = ab + b
print(c)            #元组之间相加，产生的仍然是元组

print(len(c))
print(sum(c))
print(max(c))       #元素的长度，加，最大，最小
print(min(c))

a = [10,20,30]
b = [40,50,60]
c = [70,80,90]
d = zip(a,b,c)      #通过zip可以将多个列表压缩成为元组，再转化为列表
print(list(d))
print(type(d))


#元组的访问与处理速度比列表快
#与整数，字符串一样，元组可以作为字典的键，而列表则不能

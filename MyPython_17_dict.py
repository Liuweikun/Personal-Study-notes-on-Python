print("字典")
#字典含有键值对，是一种无序的可变的序列
#字典中每一个元素都是一个键值对，包含一个键对象和一个值对象，可以通过
#键对象快速获取，修改，删除值对象
#键是任意不可变数据，比如整数，浮点数，字符串，元组，但是列表，字典，集合等可变对象，
#不能作为键，且键不可重复
#值是任意的数据，并且可以重复

print("字典的创建")
a = {'name':'chenyanyu','age':'18','job':'programmer'}
b = dict(name = "chenyanyu",age = 18 )
c = dict([("name","chenyanyu"),("age","18")]) #一个列表里通过元组创造键值对
d = {}
e = dict()    #空的字典对象
print(type(d))
print(type(e))

k = ["name","age"]
v = ["chenyanyu","18"]
f = dict(zip(k,v))     #通过zip创建字典
print(f,type(f))

#通过fromkeys创建值为空的字典
h = dict.fromkeys(["name","age","job"])
print(h,type(h))

print("字典的元素访问")
a = {'name':'chenyanyu','age':'18','job':'programmer'}

print(a["name"])  #访问方法一输入键，若存在，则显示值，若不存在，则抛出异常
print(a.get("name"))  #更推荐使用a.get()方法，若存在，显示值，若不存在，显示none
print(a.get("ddddd"))
print(a.items())   #遍历所有键值对
print(a.keys())    #列出所有的键
print(a.values())  #列出所有的值
print(len(a))      #列出键值对的个数
print("name" in a,"ddd" in a)  #检=检测某个键是否在键值对中，有返回True，没有则返回False





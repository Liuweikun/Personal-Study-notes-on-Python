a = 'b'
c = str(3.14e-2)  #实现数字转型为字符串
print(a + c)

print("用[]提取字符")
a = "abcdefghijklmnopqrstuvwxyz"
print(a[0])
print(a[3])
print(a[26-1])
print(a[-1])
print(a[-26])

print("replace()实现字符串替换")
#字符串本质不能替换，想要替换，只能创建新的字符串
b = a.replace("c","牛逼")    #replace("","")
print(a)
print(b)


print("字符串切片slice操作")
#可以让我们快速截取子字符串，标准格式为[start:end:step]
print(a)
print(a[2])    #提取字符串中单个字符
c = a[1:5:1]   #包头不包尾，即1 ～ （5-1）的字符串
d = a[1:8:2]
f = a[:]      #提取整个字符串
g = a[2:]     #从索引开始到结尾
h = a[:-2]    #从头开始到end-1
i = a[-3:]    #倒数三个
j = a[-8:-3]  #从-8到-4，包头不包尾
k = a[::-1]   #步长为负，表示从右向左反向提取
print(c)
print(d)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

print("test")

a = "to be or not to be"
b = a[::-1]               #要求字符串倒序输出
print(b)

c = "svgsntskfsols"
d = c[::3]                #要求将字符串中所有的s输出
print(d)


print("split()分割与join()合并")
#与slice不同，这个split用于将字符串切割成 多个 子字符串

a = "to be or not to be"
b = a.split()  #若不指定分隔符，将按照默认空白字符分割
c = a.split("to")   #指定以 to 分割
print(b)
print(c)

print("join()使用")
print(b)
d = ' '.join(b)
print(d)             #负责将多个字符串拼接成为一个字符串，与+不同，join只需要新建一次对象，数据量大时，需要用join()

print("字符串驻留机制与比较")
#字符串驻留，仅保存一份相同且不可变字符串的方法，包含_,字母，数字，会启用字符串驻留机制，与之前的数据缓存有异曲同工之妙

a = "abd_33"
b = "abd_33"
print(id(a))
print(id(b))
print(a is b)   #符合字符串驻留机制的规则，所以没有创建新的对象

c = "dd##"
d = "dd##"
print(id(c))
print(id(d))
print(c is d)   #True ,虽然不符合相应规则，但是新版本的python宽容度更高，所以也适用与驻留机制

#比较 ==，!=对字符串进行比较，比较是值是否相同

e = "abcdefg"
f = "a"
f1 = "abc"
f2 = "acd"
f3 = "eee"
print(f in e)
print(f1 in e)
print(f2 in e)
print(f3 in e)














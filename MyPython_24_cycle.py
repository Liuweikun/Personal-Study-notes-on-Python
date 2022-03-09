print("循环结构")

#循环结构是用来重复执行一条或多条语句，表达这样的逻辑
#如果符合条件，则反复执行循环体的语句，在每次执行完后会判断
#一次条件是否为True，如果为True则重复执行循环体的语句，
#循环体的语句至少应该包括改变条件表达式的语句，以使循环趋于结束
#否则，就会是一个死循环

print("while 循环")
"""
while循环语法格式：
while 条件表达式：
    循环体语句 
"""
print("用while循环打印0-10的数字")
num = 0
while num <= 10:
    print(num,end="\t")
    num += 1

print("计算1-100的累 加和")
a = 0
sum_a = 0

while a <= 100:
    sum_a += a
    a += 1
print("1-100相加之和：",sum_a)  #注意缩进，如果缩进，则是每一次计算都要写出结果

print("for 循环")
#语法格式：
"""
for 变量 in 可迭代对象：
    循环体语句

"""
for x in (20,30,40):
    x = x * 3
    print(x)

#python 可迭代对象
"""
1，序列：字符串，列表，元组
2。字典
3，迭代器对象：iterator
4，生成器函数：generator

"""
print("遍历字符串")

for x in "abcdefg":
    print(x)

print("遍历字典")
d = {"name":"chenyanyu","age":18,"job":"first love"}
print("遍历字典所有的key")
for x in d:
    print(x)

for x in d.keys():
    print(x)

print("遍历字典中所有的值")
for x in d.values():
    print(x)

print("遍历字典键值对")
for x in d.items():
    print(x)

print("range 对象")
#迭代器对象，用于产生指定范围的数字序列，格式为：
#range(start, end [,step])

for i in range(10):
    print(i,end = "\t")
print("\n")
for i in range(3,10):
    print(i,end = "\t")
print("\n")
for i in range(3,10,2):
    print(i,end = "\t")

print("利用for循环计算1-100的和")
sum_x = 0

for x in range(101):
    sum_x += x
print("1-100累计和：",sum_x)

print("利用for循环计算1-100的偶数和")

sum_y = 0
for y in range(101):
    if y % 2 == 0:
        sum_y += y
print("1-100偶数累计和：",sum_y)  #方法一

sum_y1 = 0
for y1 in range(2,102,2):
    sum_y1 += y1
print(sum_y1)                   #方法二

print("利用for循环计算1-100的奇数和")
sum_v = 0
for v in range(101):
    if v % 2 == 1:
        sum_v += v
print("1-100累计奇数和：",sum_v)    #方法一

sum_v1 = 0
for v1 in range(1,101,2):
    sum_v1 += v1
print(sum_v1)                    #方法二












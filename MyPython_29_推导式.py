print("推导式")
"""
推导式是从一个或者多个迭代器快速创建序列的方法，
可以将循环与条件判断相结合，从而避免冗长的代码
"""

print("列表推导式")
"""
格式1：
[表达式 for x in 可迭代对象]
格式2：
[表达式 for x in 迭代对象 if 条件判断]
"""
a = []
for x in range(5):       #正常表达式
    a.append(x)
print(a)

a = [x for x in range(5)]       #推导式
print(a)

a = [x*2 for x in range(20) if x%5 == 0]   #推导式
print(a)

A = [(a,b) for a in range(1,10) for b in range(1,10)]  #双重循环推导式
print(A)

print("#################################")
print("字典推导式")
""""
{key:value for x in 可迭代对象}
也可以增加if ，多重循环
"""
text = "I love 陈妍宇，I love 曹亚雄，I love 齐哲颖"
#统计每个字符出现的次数

char_count = {x:text.count(x)  for x in text}        #count() 方法用于统计字符串里某个字符或子字符串出现的次数。
                                                        # 可选参数为在字符串搜索的开始与结束位置
print(char_count)


print("###########################")
print("集合推导式")
"""
{表达式 for x in 可迭代对象}

"""
A = {a*3 for a in range(10) if a%9 == 0}
print(A)


print("#############################")
print("生成器推导式(用于生成元组)")
"""
（表达式 for x in 可迭代对象 if 表达式）
"""
A = (a*3 for a in range(20) if a%9 == 0)
print(A)     #生成器对象，元组是没有推导式的
for B in A:                #生成器就是一个可迭代的对象
    print(B,end="\t")



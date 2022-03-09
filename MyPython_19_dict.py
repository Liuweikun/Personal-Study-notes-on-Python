from random import shuffle
from re import S


print("序列解包")
print("元组解包")
x,y,z = (10,20,30)
print(x,"\n")

print("序列解包")
[a,b,c] = [10,20,30]
print(a)

print("\n字典解包")
a = {"name":"chenyanyu","age":18,"job":"programmer"}
s1,s2,s3 = a
print(s1)     #默认对键解包

s1,s2,s3 = a.items()
print(s2)     #默认对键值对解包

s1,s2,s3 = a.values()
print(s3)     #默认对值对象解包






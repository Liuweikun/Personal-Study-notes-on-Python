print("测试zip并行迭代")
#说白了，就是几个元素一起同时进行循环
for i in [1,2,3]:
    print(i)

names = ("chenyanyu","caoyaxiong","qizheyin")
ages = (18,20,22) 
jobs = ("teacher","nurse","doctor")

for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

xyz = zip(x,y,z)     #返回一个对象
print(list(xyz))

x1,y1,z1 = zip(*zip(x,y,z))
print(list(x1))
print((list(y1)))
print(list(z1))


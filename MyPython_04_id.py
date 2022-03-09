print("标识符")
#1.区分大小写
#2.必须以字母，下划线开头，后面可以为字母，数字，下划线
#3.不能使用关键字
#4.尽量避免双下划线开头和结尾

abv = 123
_abv = 123
_abv123 = 123
_abv123_ = 123
#以上命名方式均可以

#输入help（），输入keywords可以查看所有关键词


print("变量的声明与赋值")
#变量 = 表达式

a = 123
print(a)

#删除变量和垃圾回收

del a
#print(a)   这里因为已经被删除，所以无法打印

print("链式赋值")
x = y = 123
#将同一个对象，赋值给了多个变量
print(id(x))
print(id(y))

print("系列解包赋值")
a,b,c = 4,5,6
#相当于 a=4,b=5,c=6,个数必须保持一致，一一对应
print(id(a))
print(id(b))
print(id(c))


print("变量交换")
a,b = 1,2
a,b = b,a
print(a,b)

#python不支持常量，只能逻辑上不改变


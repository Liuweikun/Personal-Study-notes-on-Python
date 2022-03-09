a = "abcderasdfdfadfadfadfadfadfadf"
#   \是行连接符
b = "asdfasdfadf\
asdfadsfadfa\
asdfdfasfsa"
print(b)


print("python一切皆对象")
#每个对象由 标识 identity，类型 type，值 value组成
#ID 用于唯一标识对象，通常对应计算机内存中的地址，可以通过id(obj)返回对象obj标识
#type 表示对象存储的数据类型，可以通过type（obj）获得
#value 代表对象所存储的数据的信息，使用print 直接打印
#对象的本质：一个内存块，拥有特定的值，支持特定类型的相关操作

a = 3
print(id(3))
print(id(a))
print(type(a))
print(a)


print("引用")
#变量位于栈内存，对象位于堆内存，变量也称为对象的引用
#python是动态类型语言，不需要显式声明类型，但是是强类型语言，只支持该类型支持的操作

a = 3 + 10
#   a = 3 + "a" 这样是错误的


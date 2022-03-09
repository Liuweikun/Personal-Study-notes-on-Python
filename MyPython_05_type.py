print("基本内置数据类型")
#整型；浮点型，数字

# + = * / // % **

print(3 + 2)
print(30 - 5)
print(30 * 6)
print(8 / 2)   #0不能作为除数，会产生异常报错
print(7 // 2)  #整数除法，取整数
print(7 % 4)   #取余，取模运算，取余数
print(2 ** 3)  #幂运算
print(divmod(13,3))   #divmod()函数可以同时得到商和余数


print("整数")
print("将二进制的数字转化为十进制")
print(0b10101)  #表示将二进制的10101转化为十进制的21
print("将十进制的数字转化为二进制")
print(bin(2042))  #bin()


print("将八进制的数字转化为十进制")
print(0o10101)  #表示将八进制的10101转化为十进制的4161
print("将十进制的数字转化为八进制")
print(oct(2042)) #oct()

print("将十六进制的数字转化为十进制")
print(0x10101)  #表示将十六进制的10101转化为10进制的65793
print("将十进制的数字转化为十六进制")
print(hex(2042))  #hex()

print("使用int()实现类型转换")
print(int(9.9123))   #9 直接舍去小数部分
print(int(True))     #1
print(int(False))    #0

print("自动转型")
print(2 + 8.0)   #10.0

print("浮点数")
#3.14 可以写成314e-2 e-2代表*10-2
a = 3
print(float(a))  #3.0,新生成的对象

print(float("3.14"))  #可以将字符串转换为小数
print(round(9.9123))  #返回四舍五入的值，与之前的int直接舍去小数部分不同

print("各类增强运算符")
a = 3
a += 4
print(a)

b = 4
b -= 3
print(b)

c = 2
c *= 4
print(c)

d = 8
d /= 2
print(d)

e = 9
e //= 2
print(e)

f = 9
f %= 2
print(f)

j = 11
j **= 2
print(j)


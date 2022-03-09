print("布尔值")
#比较运算符
print( 3 == 4)  #等于
print( 3 != 4)  #不等于
print( 3 > 4)   
print( 3 < 4)
print( 3 >= 4)
print( 3 <= 4)


print("逻辑运算符")
x = True
y = False

print(x or y)   #或，从左往右判断，x为true，直接判断为true，后面的不管，如果x为false，继续判断右边的y,若y为true则为true，反之为false

print(x and y)  #与，从左向右判断，两边都必须为true才为true，否则为false

print(not x)   #非，x为true，则返回false，y为false，返回true

print("同一运算符")

#is 和 == 的区别，is比较是两个变量是不是同一个对象，而 == 比较的是两个变量的value值是否相同，而不关注是不是同一个对象

a = 10000
b = 10000  
print( a == b)
print( a is b)     #-5到任意正整数都会进行缓存，做了一部分优化，而python本身对[-5,256]范围进行优化



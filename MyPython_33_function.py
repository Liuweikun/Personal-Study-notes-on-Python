print("函数也是对象，内存底层分析")

def test01():
    print("admin")

test01()   #admin

c = test01
c()         #admin

print(id(test01))
print(id(c))
print(type(c))
print((type(test01)))      #说明为同一个对象


print("+++++++++++++全局变量与局部变量+++++++++++++++++")
"""
全局变量：
1、在函数和类定义之外声明的变量，作用域为定义的模块，从
定义位置开始直到模块结束。
2、全局变量降低了函数的通用性和可读性，应尽量避免全局变量的使用
3、全局变量一般做常量使用
4、函数内要改变全局变量的值，使用global声明一下

局部变量：
1、在函数体中(包含形式参数)声明的变量
2、局部变量的引用比全局变量快，优先考虑使用
3、使用局部变量和全局变量同名，则隐藏全局变量，只使用同名的局部变量


"""

a = 3         #全局变量

def test01():
    b = 4             #局部变量
    print(b * 4 + a)  #全局变量可以在函数内使用


print(a)
test01()
print(a)
test01()
#print(b)       name 'b' is not defined,局部变量在外面不能用

def test02():
    a = 300       #当局部变量和全局变量重名时，函数内优先定义为局部变量
    print(a)

    print(locals())
    print(globals())        #输出局部变量和全局变量

test02()
print(a)        #脱离了函数内自定义后，a仍然代表全局变量



def test03():
    global a         #若要在函数内部改变全局变量，硬要用，则需要声明
    a = 400
    print(a)

test03()
print(a)




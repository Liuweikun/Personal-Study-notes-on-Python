print("lambda表达式和匿名函数")
"""
lambda表达式可以声明匿名函数，是一种简单的，在同一行就定义了函数的方法
实际生成一个函数对象，只允许包含一个表达式，不能包含复杂语句，

lambda arg1,arg2,arg3……:表达式
arg1/arg2/arg3为函数的参数，表达式相当于函数体，运算结果就是表达式的运算结果


"""
test01 = lambda a,b,c:a+b+c
print(test01)
print(test01(2,3,4))
print()

test02 = [lambda a:a*2,lambda b:b*3,lambda c:c*3]
print(test02[0](6),test02[1](7),test02[2](8))     #复杂变化

print("函数也是对象")
def test03(a,b,c):

    return a*b*c

f = [test03,test03]
print(f[0](3,4,5))


print("\neval")
"""
功能：将字符串str当成有效的表达式来求值来返回计算结果
语法：eval(source[,globals,[locals]] -> value)
参数：
    source：一个Python表达式或者函数compile()返回的代码对象
    globals：可选，但必须是dictionary
    locals：可选，任意映射对象


"""

dict1 = dict(a = 100,b = 200)
d = eval("a + b",dict1)
print(d)


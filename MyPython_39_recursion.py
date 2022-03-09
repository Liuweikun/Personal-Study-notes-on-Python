
print("递归函数")
"""
递归函数指的是：自己调用自己的函数，在函数体内部直接或者间接地自己调用自己
包含两部分
1，终止条件
   表示递归什么时候结束，一般用于返回值，不再调用自己
2，递归步骤
   把第N步的值和第N-1步相关联

会大量的创建函数对象，过量的消耗内存和运算能力，处理大量数据时，谨慎使用

"""

def test01():
    print("test01")
#    test01()  递归了，


def test02(n):
    print("test02:",n)
    if n != 0:
        test02(n-1)     #设置终止条件，将N与N-1相关联
    else:
        print("over")

test02(5)


print("递使用递归函数计算阶乘")
def test03(n):

    if n == 1:
        return 1
    else:
        return n * test03(n-1)

result = test03(4)
print(result)


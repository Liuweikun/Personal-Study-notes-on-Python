print("单分支选择结构")
#结构示意图详情见WPS"选择结构流程图"
"""
if 条件表达式:
    语句/语句块
条件表达式：可以是逻辑表达式，关系表达式，算术表达式
语句/语句块：可以是一条语句，也可以是多条语句，且必须有缩进，对齐
"""

print("输入一个数字，若小于10则打印这个数字，否则不打印")
a = 3
if a < 10:
    print(a)

num1 = 6
if num1 < 10:                      #需要将字符串转化为int类型
    print(num1,"是小于10的数字")

print("\n条件表示式详解")
"""
在选择和循环结构中，条件表达式值为false的情况如下：
False、0、0.0、空值None、空序列对象、空range对象、空迭代对象
其他情况，均为True
"""
if 3:
    print("ok\n")   #若输入为0则无法运行代码，因为为false

a = []
if a:
    print("空列表，False\n")  #结果打印不出来，走了false

if not a:
    print("空列表，False\n")  #结果可以打印因为if not

s = "False"
if s:
    print("非空字符串，是True\n")

c = 9
if 3 < c < 20:
    print("3 < c < 20\n")

if True:
    print("True\n")

#python 中不允许有赋值操作符"="

print("双分支选择结构")

"""
if 条件表达式：
    语句1/语句块1
else：
    语句2/语句块2
"""
print("输入一个数字，小于10 ，则打印该数字，大于10，则打印数字太大")
num = input("输入一个数字：")
if int(num) < 10:
    print(num)
else:
    print("该数字不小于10\n")

print("三元运算符")
"""
条件为真时输出的结果 if （条件表达式） else 条件为假时的值

"""
num = input("请输入一个数字：")
print(num if int(num) < 10 else "数字太大")
#这里的num 为条件为真时的结果，后面的"数字太大"为条件为假的值














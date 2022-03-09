print("位置参数")
def test01(a,b,c):
    print(a,b,c)

test01(1,2,3)
#  test01(2,3)        参数个数不匹配报错
# TypeError: test01() missing 1 required positional argument: 'c'


print("\n默认值参数")
#我们可以为某些参数设置默认值，这些参数在传递时是可选的，称为默认值参数，
#默认值参数位于位置参数后面

def test02(a,b,c = 10,d = 20):      #c=10,d = 20就是默认值参数，必须在位置参数后面
    print(a,b,c,d,)

test02(5,6)
test02(5,6,7)
test02(5,6,7,8)

print("\n命名参数")
def test03(a=10,b=20,c=30,d=40):      #这是命名参数，通过形参名称来匹配
    print(a,b,c,d)

test03()
test03(1,2,3,4)

print("\n可变参数")
"""
*param为可变参数的一种，意义为将多个参数收集起来为一个"元组"对象
**param为可变参数的一种，意义为将多个参数收集起来为一个"字典"对象
"""

def test04(a,b,*c):
    print(a,b,c)

test04(1,2,19,20)       #这里的19，20就被划分到*C，成为一个元组

def test05(a,b,**c):
    print(a,b,c)

test05(10,20,name = "chenyanyu",ID = "love")   #两个星号就可变参数的第二种

def test06(a,b,*c,**d):
    print(a,b,c,d,)

test06(10,20,30,40,50,name = "chenyanyu",id = "love",age = "18")   #两种可变参数混合

print("\n强制命名参数")
#在带星号的可变参数后增加新的参数，必须是强制命名参数
def test07(*a,b,c):
    print(a,b,c)

#test07(10,20,30)    会报错，由于a是可变参数，如果没有强制命名参数，会导致后面的bc没有参数可以添加
test07(10,b = 20,c = 30)




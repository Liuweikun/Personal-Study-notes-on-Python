import copy

print("浅拷贝和深拷贝")
"""
内置函数：copy(浅拷贝)、deepcopy(深拷贝）
浅拷贝：不拷贝子对象的内容，只拷贝子对象的引用
深拷贝：会对子对象的内存也全部拷贝一份，对子对象的修改不影响源对象

"""
print("++++++++++++++++++++浅拷贝++++++++++++++++++++")
def testcopy01():
    a = [10,20,[5,6]]
    b = copy.copy(a)               #浅拷贝，只拷贝对象的引用
    print("a:",a)
    print("b:",b)                  #拷贝完

    b.append(30)
    b[2].append(7)

    print("a:",a)            #30没有算进去
    print("b:",b)            #7算进去了，因为原有的引用已经改变了

testcopy01()
print("+++++++++++++++++深拷贝+++++++++++++++++")
def testdeepcopy01():
    c = [10,20,[5,6]]
    d = copy.deepcopy(c)        #纯粹复制拷贝，完全拷贝
    print("c:", c)
    print("d:", d)  # 拷贝完

    d.append(30)
    d[2].append(7)

    print("c:", c)  # 7,30均没有算进去
    print("d:", d)  # 7算进去
testdeepcopy01()



print("传递不可变对象")
"""
例如float，int，字符串，元组，布尔值
传递不可变对象时，如果子对象是可变对象， 则方法内修改了这个可变对象
源对象也发生了变化 

"""

a = (50,60,[1,2])       #定义一个元组，属于不可变对象
print("a的ID：",id(a))

def test01(m):
    print("m的ID：",id(m))

    m[2][0] = 888      #元组对象不可变，但是具体到元组里面的列表对象是可变的，可替换的，本质是浅拷贝
    print(m)
    print("m的ID：",id(m))

test01(a)
print(a)

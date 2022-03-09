import time
import math

print("++++++++++++全局变量与局部变量效率对比+++++++++++++++")
"""
局部变量查询，访问速度均比全局变量快，优先使用，尤其是循环时
在特别强调效率的地方，和循环次数多的地方，可以将全局变量转为局部变量提升速度
"""

print("使用全局变量效率：")
def test01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时：{0}".format(start))
    print("耗时：{0}".format(end))
"""

    print("耗时{0}".format(end - start))
    print("耗时{0}".format((end - start)))
    print("耗时{0}",end - start)
    print("耗时{0}",(end - start))


"""

test01()
print(1643972029.080262 - 1643972028.545124)

def test02():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时{0}".format(end - start))

test02()

def test03():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时{0}".format((end - start)))

test03()

def test04():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时",end - start)         #这种方式耗时最短

test04()

def test05():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时",(end - start))

test05()

def test06():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("全局变量直接带入耗时",end - start)
test06()

def test07():
    b = math.sqrt
    start = time.time()
    for i in range(10000000):
        b(30)
    end = time.time()
    print("全局变量先变局部变量耗时",end - start)
test07()

def test08():
    b = math.sqrt
    start = time.time()
    for i in range(10000000):
        b(30)
    end = time.time()
    print("全局变量先变局部变量耗时{0}".format((end - start)))

test08()
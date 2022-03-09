print("循环优化技巧")
print("1.尽量减少循环内部不必要的计算")
print("2.嵌套循环中，尽量减少内部循环的计算，尽量往外提")
print("3.局部变量查询较快，尽量使用查询变量")
import time
start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000 + m*100)

end = time.time()
print("耗时：{0}".format((end - start)))

start2 = time.time()
for i in range(1000):
    result = []
    c = i * 1000
    for m in range(10000):
        result.append(c + m*100)

end2 = time.time()
print("耗时：{0}".format((end2-start2)))

print("连接多个字符串，尽量使用join(),而不使用+")
print("列表进行元素插入和删除，尽量在列表尾部操作")


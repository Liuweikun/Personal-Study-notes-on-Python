print("循环里的else")
#如果for和while后面没有被break，则执行之后的else语句，
#如果被break，则不执行else
"""
while 条件表达式：
    循环体
else：
    语句块

或 for in 可迭代对象：
    循环体
else：
    语句块
"""

print("录入四个人的薪资，全部录入后显示全部录入完成，并且打印薪资列表和平均薪资")
salarySum = 0           #总薪资
salarys = []            #薪资列表

for i in range(4):        #个人薪资
    s = input("请输入个人薪资(若要中途结束请摁'T/t')：")

    if s.upper() == "T":                #循环过程中出现中断的情况，停止所有循环
        print("录入中途完成，请退出")
        break

    if float(s) < 0:                    #循环过程中出现输错的情况，停止本次循环，
        continue
    salarys.append(float(s))
    salarySum += float(s)

else:                                    #全部循环完后，没有被中途break的情况
    print("您已全部录入四名员工工资")


print("录入薪资:{0}".format(salarys))
print("平均薪资:{0}".format(salarySum/4))



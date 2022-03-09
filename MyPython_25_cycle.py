print("嵌套循环")
#一个循环体嵌入另一个循环体，形成多重循环，也叫嵌套循环
print("打印以下图案：")
for x in range(0,5):          #当x=0时就进入循环
    for y in range(0,5):      #将x = 0 循环5次，按第一次进入
        print(x,end="\t")     #循环到这里 ，x 加空格符
    print()                   #自动换行


print("用嵌套循环打印99乘法循环表")
for y in range(1,10):
    for x in range(1,y+1):        #y + 1 理解有困难
        print("{0} * {1} = {2}".format(x,y,x*y),end="\t")
    print()

print("存储数据，并打印表格中工资高于15000的数据")
r1 = {"name":"chenynayu","age":18,"job":"As My first love","city":"北京","salary":30000}
r2 = {"name":"caoyaxiong","age":18,"job":"As My second love","city":"上海","salary":20000}
r3 = {"name":"qizheyin","age":18,"job":"As My third love","city":"广州","salary":10000}
tb = [r1,r2,r3]

for x in tb:
    if x.get("salary") > 15000:
        print(x)

print("#####################################")
print("break 语句:")
#break 可以用于for循环和while循环，用于结束整个循环！
#当出现嵌套时，则只能跳出最近一层的循环
while True:
    a = input("请输入Q或者q结束：")
    if a.upper() == 'Q':
        print("结束！")
        break
    else:
        print(a)

print("###################################")
print("continue 语句")
#用于结束本次循环，继续下一次。多个循环嵌套时，应用于最近的一层循环


print("输入员工薪资，小于0就重新输入，最后打印员工数量，薪资明细，平均薪资")
empNum = 0            #员工数量
salarys = []          #员工工资列表
salarySum = 0         #所有员工薪资相加总和
while True:
    s = input("请输入一名员工的薪资(输完后请按T/t结束): ")        #单个员工薪资，无限循环

    if s.upper() == "T":                        #一直等输入完成，如果中断，停止所有循环
        print("录入完成，退出")
        break

    if float(s) < 0:                            #如果薪资小于0，则重新开始循环输入，停止本次循环
        continue

    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数量:{0}".format(empNum))
print("员工薪资明细：",salarys)
print("员工平均工资:{0}".format(salarySum/empNum))         #平均工资 = 总工资/员工数量


print("break 和 continue对比")
for i in range(1,5):
    if i != 3:
        print(i)
    else:
        break     #1,2是因为循环到了1，2，中断了循环

for i in range(1,5):
    if i != 3:
        print(i)
    else:
        continue       #1，2，4，跳过了3循环




















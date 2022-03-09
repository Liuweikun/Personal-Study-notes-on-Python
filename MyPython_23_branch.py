print("多分支结构")
"""
语法结构：
if 条件表达式1：
    语句1/语句块1
elif 条件表达式2：
    语句2/语句块2
.
.
.
elif 条件表达式n:
        语句n/语句块n
[else:
        语句n/语句块n+1
] 

"""
print("输入一个学生的成绩，将其转化为简单描述："
      "不及格(小于60)、及格(60-79)，良好(80-89),优秀(90-100)")

results = int(input("请输入学生分数："))
grade = ""
if 0 <= (results) < 60:
    grade = "不及格"
elif 60 <= (results) < 80:
    grade = "及格"
elif 80 <= (results) < 90:
    grade = "良好"
elif 90 <= (results) < 101:
    grade = "优秀"
else:
    grade = "无效成绩，请确认后重新输入"

print("该生成绩为{0},为{1}!".format(results,grade))

print("\n练习：已知坐标（x,y）,判断其所在象限")

x = int(input("请输入横坐标："))
y = int(input("请输入纵坐标："))
result = ""

if x == 0 and y == 0:
    result = "原点"
elif x == 0 and y != 0:
    result = "X轴上"
elif x != 0 and y == 0:
    result = "y轴上"
elif x > 0 and y > 0:
    result = "第一象限"
elif x > 0 and y < 0:
    result = "第四象限"
elif x < 0 and y > 0:
    result = "第二象限"
else:
    result = "第三象限"

print("坐标为({0},{1}),位于{2}".format(x,y,result))

import turtle


print("画一个不同颜色的同心圆")
t = turtle.Pen()  #t代表画笔，获得画笔
t.width(20)          #画笔粗细
t.speed(0)          #速度为0速度最快
my_colors = ("red","blue","green","orange")
for i in range(120):     #画5次圆，    0 ，1 ，2， 3， 4
    t.penup()
    t.goto(0,-i * 10)  #确定圆起始笔：0，-50，-100，-150，-200
    t.pendown()
    t.circle((i+1)*10)       #确定圆的的半径：50，100，150，200，250
    t.color(my_colors[i%len(my_colors)])



"""
t.circle(100)
t.penup()
t.goto(0,-100)
t.pendown()
t.circle(200)

t.penup()
t.goto(0,-200)
t.pendown()
t.circle(300)

t.penup()
t.goto(0,-300)
t.pendown()
t.circle(400)

"""





"""


t.penup()
t.goto(0,-50)
t.pendown()
t.circle(100)

t.penup()
t.goto(0,-100)
t.pendown()
t.circle(150)

t.penup()
t.goto(0,-150)
t.pendown()
t.circle(200)

"""







turtle.done()           #画完后，让画停留
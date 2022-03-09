import turtle

print("画棋盘")

t = turtle.Pen()
t.speed(0)


for x in range(19):
    t.penup()
    t.goto(-180,-180+(x*20))
    t.pendown()
    t.forward(360)
t.right(90)
for x in range(19):
    t.penup()
    t.goto(-180+(x*20),180)
    t.pendown()
    t.forward(360)
"""
t.penup()
t.goto(-180,180)
t.pendown()
t.forward(360)
"""








turtle.done()


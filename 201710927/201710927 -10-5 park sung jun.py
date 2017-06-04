


import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


width=wn.window_width()


x1=0.0 -(width -40)/3
x2=0.0
x3=0.0 +(width -40)/3

w3=(width -40)/3
x1=0.0-w3
x2=0.0
x3=0.0+w3



t1.heading()




def Triangle(size):
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
    

def drawTriangleAt(size,pos):
    t1.penup()
    t1.goto(x1,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    Triangle(size)

def Pentagon(size):
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)

def drawPentagonAt(size,pos):
    t1.penup()
    t1.goto(x2,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    Pentagon(size)

def Star(size):
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    

def drawStarAt(size,pos):
    t1.penup()
    t1.goto(x3,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    Star(size)

drawTriangleAt(100,x1)
drawPentagonAt(100,x2)
drawStarAt(100,x3)

wn.exitonclick()

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def giyukAt(size):
   
   
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)


def niuenAt(size):
   

    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)


def miumAt(x,y,size):
    t1.penup()

    t1.goto(x,y)
    t1.pendown()
    giyukAt(size)
    t1.penup()
    t1.bk(size)
    t1.lt(90)
    t1.bk(size)
    t1.pendown()
    niuenAt(size)

miumAt(-100,100,100)

wn.exitonclick()

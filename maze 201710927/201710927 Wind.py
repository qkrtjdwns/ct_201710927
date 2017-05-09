import turtle

wn=turtle.Screen()
t1=turtle.Turtle()

size=100
def giyuk(size):
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)

pos1=(0,0)
pos2=(50,-50)

turnBy=45
size=100

oldPos=t1.pos()
oldHead=t1.heading()
giyuk(100)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy)
t1.pendown()
giyuk(size)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy*2)
t1.pendown()
giyuk(size)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy*3)
t1.pendown()
giyuk(size)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy*4)
t1.pendown()
giyuk(size)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy*5)
t1.pendown()
giyuk(size)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy*6)
t1.pendown()
giyuk(size)

t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBy*7)
t1.pendown()
giyuk(size)
wn.exitonclick()







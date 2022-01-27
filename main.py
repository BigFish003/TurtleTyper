import random
import time
import turtle
e = turtle
e.penup()
e.speed(300)
length = 1
xposition = -330
yposition = -300
spacedex = 30
size = 25
def up():
    e.setheading(90)
    e.forward(size)
def down():
    e.setheading(270)
    e.forward(size)
def left():
    e.setheading(180)
    e.forward(size)
def right():
    e.setheading(0)
    e.forward(size)
def big():
    global size
    global spacedex
    size += 1
    spacedex += 1
def small():
    global size
    global spacedex
    size -= 1
    spacedex -= 1
def zero():
    global xposition
    global spacedex
    xposition += spacedex
    e.pendown()
    right()
    up()
    up()
    left()
    down()
    down()
    e.penup()
    e.goto(xposition, -300)
def one():
    global xposition
    global spacedex
    xposition += spacedex
    right()
    e.pendown()
    up()
    up()
    e.penup()
    e.goto(xposition, -300)
def two():
    global xposition
    global spacedex
    xposition += spacedex
    right()
    e.pendown()
    left()
    up()
    right()
    up()
    left()
    e.penup()
    e.goto(xposition, -300)
def three():
    global xposition
    global spacedex
    xposition += spacedex
    e.pendown()
    right()
    up()
    left()
    right()
    up()
    left()
    e.penup()
    e.goto(xposition, -300)
def four():
    global xposition
    global spacedex
    xposition += spacedex
    right()
    e.pendown()
    up()
    left()
    up()
    down()
    right()
    up()
    e.penup()
    e.goto(xposition, -300)
def five():
    global xposition
    global spacedex
    xposition += spacedex
    e.pendown()
    right()
    up()
    left()
    up()
    right()
    e.penup()
    e.goto(xposition, -300)
def six():
    global xposition
    global spacedex
    xposition += spacedex
    e.pendown()
    right()
    up()
    left()
    down()
    up()
    up()
    right()
    e.penup()
    e.goto(xposition, -300)
def seven():
    global xposition
    global spacedex
    xposition += spacedex
    right()
    e.pendown()
    up()
    up()
    left()
    e.penup()
    e.goto(xposition, -300)
def eight():
    global xposition
    global spacedex
    xposition += spacedex
    e.pendown()
    right()
    up()
    up()
    left()
    down()
    right()
    left()
    down()
    e.penup()
    e.goto(xposition, -300)
def nine():
    global xposition
    global spacedex
    xposition += spacedex
    right()
    e.pendown()
    up()
    up()
    left()
    down()
    right()
    e.penup()
    e.goto(xposition, -300)
def Type():
    e.setposition(-330, -300)
    e.penup()
    e.listen()
    e.onkey(zero, "0")
    e.onkey(one, "1")
    e.onkey(two, "2")
    e.onkey(three, "3")
    e.onkey(four, "4")
    e.onkey(five, "5")
    e.onkey(six, "6")
    e.onkey(seven, "7")
    e.onkey(eight, "8")
    e.onkey(nine, "9")
    e.onkey(big, "e")
    e.onkey(small, "q")
    e.mainloop()
    time.sleep(5)
Type()
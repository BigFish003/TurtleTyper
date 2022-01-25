import random
import time
import turtle
e = turtle
e.penup()
e.speed(100)
length = 1
xposition = -330
yposition = -300
spacedex = 1
def wait(sec):
    time.sleep(sec)
def one():
    global xposition
    xposition += 40
    e.pendown()
    e.setheading(90)
    e.forward(50)
    e.setheading(200)
    e.forward(10)
    e.penup()
    e.goto(xposition, -300)
def two():
    global xposition
    xposition += 15
    e.pendown()
    e.setheading(180)
    e.forward(25)
    e.setheading(70)
    e.forward(55)
    e.setheading(180)
    e.forward(25)
    e.setheading(270)
    e.forward(15)
    e.penup()
    e.goto(xposition, -300)
def three():
    global xposition
    xposition += 40
    e.pendown()
    e.setheading(0)
    e.forward(25)
    e.setheading(90)
    e.forward(25)
    e.setheading(180)
    e.forward(25)
    e.setheading(0)
    e.forward(25)
    e.setheading(90)
    e.forward(25)
    e.setheading(180)
    e.forward(25)
    e.penup()
    e.goto(xposition, -300)
def four():
    global xposition
    xposition += 30
    e.setheading(0)
    e.forward(25)
    e.pendown()
    e.setheading(90)
    e.forward(50)
    e.setheading(270)
    e.forward(25)
    e.setheading(180)
    e.forward(25)
    e.setheading(90)
    e.forward(25)
    e.penup()
    e.goto(xposition, -300)
def Type():
    e.setposition(-330, -300)
    e.penup()
    e.listen()
    e.onkey(one, "1")
    e.onkey(two, "2")
    e.onkey(three, "3")
    e.onkey(four, "4")
    e.mainloop()
    wait(5)
Type()

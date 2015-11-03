#-------------------------------------------------------------------------------
#
# Author:      Roland Junior Toussaint
#
# Created:     14/03/2014
# Copyright:   (c) toussaintr 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
import random
import Tkinter
import os

#setheading(random.randrange(0, 360, 90))
#wn.setworldcoordinates(0,0,1000,1000)
#robber.onclick(forward, 3)

turtle.setup(700,600)
wn = turtle.Screen()
wn.title("Crazy Art")

cop = turtle.Turtle()
cop.shape('turtle')
cop.color('blue')

robber = turtle.Turtle()
robber.shape('turtle')
robber.color('red')
#robber.setpos(320,280)
robber.setpos(10,0)

def robber_move(turtle):
    fifty_fifty = random.randrange(0, 2)
    if fifty_fifty == 0:
        turtle.right(90)
    else:
        turtle.left(90)
    turtle.forward(10)

def collision(turtle1, turtle2):
    X1 = turtle1.xcor()
    Y1 = turtle1.ycor()
    X2 = turtle2.xcor()
    Y2 = turtle2.ycor()
    pos1 = (int(X1), int(Y1))
    pos2 = (int(X2), int(Y2))
    if pos1 <= pos2:
        crash = False
    else:
        crash = True
        return crash


def h1():
   cop.forward(10)

def h2():
    cop.left(90)

def h3():
    cop.right(90)

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")

if collision(cop,robber) == False:
    turtle.write("Home = ", True, align="center")


wn.listen()




Tkinter.mainloop()
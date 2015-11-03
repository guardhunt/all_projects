#-------------------------------------------------------------------------------
# Name:      Roland Junior Toussaint
# Purpose:
#
# Author:      Roland Junior Toussaint
#
# Created:     20/01/2014
# Copyright:   (c) toussaintr 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle               # allows us to use the turtles library
import random

wn = turtle.Screen()        # creates a graphics window--needed for a clean close
a = turtle.Turtle()
a.fillcolor('forest green')
a.pencolor('blue') # Set the color that myturtle.
wn.bgcolor('blue')  #Set the color of the background
a.speed(0)

#Creates the ground
a.shape('square')
a.shapesize(stretch_wid=15, stretch_len=50, outline=0)      # Makes the square huge
a.penup()
a.setpos(0,-150)        #Moves square so it is the ground
a.pendown()
a.stamp() # Stamp a copy of the turtle shape onto the canvas at the current turtle position

#House
a.pencolor('black') # Makes house outline black
a.penup()
a.setpos(0,-20)     #Determines location on map
a.pendown()
#Chimney
a.shape('square')
a.shapesize(stretch_wid=22, stretch_len=2, outline=0)
a.fillcolor('grey')
a.stamp()
#Main building
a.fillcolor('white') #color of second circle
a.shape('circle') # makes igloo
a.shapesize(stretch_wid=20, stretch_len=20, outline=0)
a.stamp()
#Door outline
a.setpos(0,10)
a.color('white')
a.pencolor('black')
a.shape('circle')       #Creates border around door
a.shapesize(stretch_wid=10, stretch_len=7, outline=0)
a.stamp()
#Create door
a.setpos(0,10)
a.color('black')
a.shape('circle')#creates door
a.shapesize(stretch_wid=8, stretch_len=5, outline=0)
a.stamp()
#Create ground for house
a.setpos(0,-150)
a.color('forest green')
a.shape('square')
a.shapesize(stretch_wid=12, stretch_len=30, outline=0)
a.stamp()

#Create flowers
a.shape('arrow')
a.shapesize(stretch_wid=1, stretch_len=1, outline=0)
a.pencolor('green') #Sets the color of the stem
a.penup()
a.forward(200)
a.left(90)
a.pendown()
#Flower
a.pensize(3)    #Thickness of flower
a.forward(35)
a.right(90)
a.forward(5)
a.right(190)
a.pencolor('pink')  # Color of outline of flower
a.fillcolor('purple')   # Internal color of flower
a.begin_fill()  # Fills the flower
for i in range(7):
    a.left(120)
    for i in range(20):
            a.forward(2)
            a.left(15)
a.end_fill() # The figure drawn between the two fill commands is filled with the present color setting



#Create Sun
a.hideturtle()
a.penup()
a.home()
a.setpos(200,180)
a.color('yellow')       #sun color
a.pendown()
a.begin_fill()
a.circle(50) # Draws a circle of the indicated radius. Assuming the radius is positive, the circle is drawn tangent to the direction of myturtle in a clockwise direction.
a.end_fill()

#Create Smoke
a.penup()
a.home()
a.pensize(3)
a.left(90)
a.forward(200)      #Height above chimney smoke starts
a.pendown()         #This is the code to get the turtle to top of the chimney
a.color('black')
a.right(180)
a.forward(5)
for i in range(7):
    a.right(50)
    a.forward(1)
    for i in range(20):
            a.forward(7)
            a.right(15)

wn.exitonclick()
#-------------------------------------------------------------------------------
# Author:      Roland Junior Toussaint
#
# Created:     18/01/2014
# Copyright:   (c) toussaintr 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle               # allows us to use the turtles library
import random

wn = turtle.Screen()        # creates a graphics window--needed for a clean close
a = turtle.Turtle()
a.fillcolor('red')
a.pencolor('blue') # Set the color that myturtle.
wn.bgcolor(random.random(),random.random(), random.random())

a.shape("arrow") # May use the following polygon shapes: "arrow", "circle", "classic", "square", "triangle", "turtle"
a.shapesize(stretch_wid=1, stretch_len=1, outline=0)
a.stamp() # Stamp a copy of the turtle shape onto the canvas at the current turtle position
a.forward(50)
a.write('Holy Shit Black Balls') # Write a string starting at the present myturtle point.
a.right(90)
a.forward(120)
a.begin_fill()
a.circle(12)
a.end_fill() # The figure drawn between the two fill commands is filled with the present color setting.
a.left(90)
a.forward(100)
wn.exitonclick()

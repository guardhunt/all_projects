######################################################################
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# Objectives:
#- Introduces the use of the turtles library
######################################################################
# Acknowledgements:
# modified by Dr. Jan Pearce
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library
import random               # allows for use of random library
wn = turtle.Screen()        # creates a graphics window--needed for a clean close

turtle = turtle.Turtle()


turtle.shape('turtle')      #Determines turtle shape
#myturtle.hideturtle()

turtle.write('Six Star') # Write a string starting at the present myturtle point.
head=0
turtle.speed(5)     # Turtle Speed
turtle.setheading(head)
turtle.pensize(5)
for j in range (100):       #Number of stars to make
    turtle.color(random.random(),random.random(), random.random())  #Randomly changes turtle color
    wn.bgcolor(random.random(),random.random(), random.random())    #randomly changes bg color
    for j in [0,1,2]:           #Creates first triangle
        turtle.forward(150)
        turtle.right(120)
    turtle.penup()              #Moves turtle to start second triangle
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(86.6)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(180)
    turtle.pendown()
    for j in [0,1,2]:           #Creates second triangle
        turtle.forward(150)
        turtle.left(120)
    turtle.penup()              #Returns to start of large loop
    turtle.left(90)
    turtle.forward(86.6)
    turtle.right(90)
    turtle.pendown()






wn.exitonclick()            # Added by Dr. Pearce to wait for a user click on the canva
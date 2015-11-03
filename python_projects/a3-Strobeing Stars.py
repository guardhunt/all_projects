######################################################################
# Modified by Roland Junior Toussaint
# username: toussaintr
#
# Assignment: A3
# Purpose: To practice with loops and turtles
#######################################################################
# Acknowledgements:
# modified by Dr. Jan Pearce
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library
import random

wn = turtle.Screen()        # creates a graphics window--needed for a clean close
          # learned this from Kristian Toole to set background color

myturtle = turtle.Turtle()      #Turtle Names
t = turtle.Turtle()
a = turtle.Turtle()

myturtle.shape('turtle')    #Turtle Shape
t.shape('turtle')
a.shape('turtle')



myinput = raw_input('What size star would you like? Please give a number')  #Number to determine star size
r = int(myinput)    # This is the distace moved forward by turtle in star.

#myturtle.hideturtle()
for i in range (8):

    head=0                    # initial heading for turtle
    myturtle.speed(70)                    # initial heading speed for turtle
    myturtle.setheading(head)
    myturtle.pensize(5)
    for i in range (45):
        wn.bgcolor(random.random(),random.random(), random.random())
        for i in [0,1,2,3,4]:           # First circle of stars and how many to make
            myturtle.color(random.random(),random.random(), random.random())      #Turtle Color
            a.color(random.random(),random.random(), random.random())       # Loops all three star patterns and lays them on top of eachother
            t.color(random.random(),random.random(), random.random())
            myturtle.forward(r)           # tell myturtle to move forward by users inputed number
            myturtle.right(144)               # turn by 144 degree
        myturtle.backward(r * 2)            # Move away from created star using users input
        myturtle.right(70)                  # turn by 70 degrees
    head=120
    t.speed(80)                    # initial speed for turtle
    t.setheading(head)
    t.pensize(5)
    for i in range(70):
        wn.bgcolor(random.random(),random.random(), random.random())
        for i in [0,1,2,3,4]:           # Second circle of stars
            myturtle.color(random.random(),random.random(), random.random())      #Turtle Color
            a.color(random.random(),random.random(), random.random())       # Loops all three star patterns and lays them on top of eachother
            t.color(random.random(),random.random(), random.random())
            t.forward(r + 10)           # tell myturtle to move forward by users inputed number plus 10
            t.right(144)               # turn by 144 degree
        t.backward(r * 2)               # Move away from created star using users input
        t.right(61)                     # turn by 61 degrees
    head=240
    a.speed(50)                    # initial speed for turtle
    a.setheading(head)
    a.pensize(5)
    for i in range(80):
        wn.bgcolor(random.random(),random.random(), random.random())
        for i in [0,1,2,3,4]:           # Third circle of stars
            myturtle.color(random.random(),random.random(), random.random())      #Turtle Color
            a.color(random.random(),random.random(), random.random())       # Loops all three star patterns and lays them on top of eachother
            t.color(random.random(),random.random(), random.random())
            a.forward(r + 15)           # tell myturtle to move forward by users inputed number plus 15
            a.right(144)               # turn by 144 degree
        a.backward(r * 2)               # Move away form created star using users input
        a.right(59)                     # turn by 59 degrees
wn.exitonclick()            # Added by Dr. Pearce to wait for a user click on the canva
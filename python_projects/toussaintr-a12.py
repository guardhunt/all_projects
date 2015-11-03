######################################################################
# Author: Roland Junior Toussaint
# username: toussaintr
# Assignment: A12
# Purpose: Practice using and creating Turtle events. Particularly on
# on key commands and on screen clicks. It creates a bizarre image of
# four differant turtles and their lines.
######################################################################
# Acknowledgements:
#   Structured after code written in How to Think Like a Computer
# Scientist: Learning with Python 3 Documentation.
# Code retreived from:
# http://cs.berea.edu/courses/csc226/tasks/turtle-onclick-example-from-text.py
# http://cs.berea.edu/courses/csc226/tasks/a12.interactive.graphics.html
######################################################################
import Tkinter      # needed for the mainloop() function
import random
import turtle

turtle.setup (width=.97,)
turtle.setup(700,600)                # Determine the window size
turtle.setup (width=.99,)

wn = turtle.Screen()                 # Get a reference to the window
wn.title("Use the arrows keys to move turtles, or click on the screen for chaos, press q to quit,")
wn.bgcolor('dark grey')             # Set the background color


steve = turtle.Turtle() # Turtle steve
steve.color('purple') # Turtle color
steve.shape('turtle') # Turtle shape
steve.pensize(2) # Pensize

crazy = turtle.Turtle() # Turtle crazy
crazy.color('green')
crazy.shape('turtle')
crazy.pensize(2)
crazy.setheading(90) # Tells turtle initial heading

that_guy = turtle.Turtle() # Turtle that_guy
that_guy.color('blue')
that_guy.shape('turtle')
that_guy.pensize(2)
that_guy.setheading(180)

bottom = turtle.Turtle() # Turtle bottom
bottom.color('red')
bottom.shape('turtle')
bottom.pensize(2)
bottom.setheading(270)
####################################################################
# Functions
def forward(): # Calls the four turtles to move forward 30 and changes everythings color
    wn.bgcolor(random.random(),random.random(),random.random()) # Changes background color random
    steve.color(random.random(),random.random(),random.random()) # Changes Turtles colors
    that_guy.color(random.random(),random.random(),random.random())
    crazy.color(random.random(),random.random(),random.random())
    bottom.color(random.random(),random.random(),random.random())
    steve.forward(30)
    that_guy.forward(30)
    crazy.forward(30)
    bottom.forward(30)

def left(): # Calls the four turtles to turn left 45
    steve.left(45)
    that_guy.left(45)
    crazy.left(45)
    bottom.left(45)

def right(): # Calls the four turtles to move left 45
    steve.right(45)
    that_guy.right(45)
    crazy.right(45)
    bottom.right(45)

def move(x, y): # Tells turtles to goto x, y cordinates
    steve.goto(x, y)
    that_guy.goto(-x,-y)

def quit(): # Closed wn screen
    wn.bye()
####################################################################
# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(forward, "Up") # Assigns funtion to Up key
wn.onkey(left, "Left") # Assigns funtion to Left key
wn.onkey(right, "Right") # Assigns funtion to Right key
wn.onkey(quit, "q") # Assigns funtion to q key

wn.onclick(move, 3) # Calls funtion when mouse clicked
wn.onclick(move, 1)

wn.listen() # Listens for the key inputs

Tkinter.mainloop() # Cleanly closes the window

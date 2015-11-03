######################################################################
# Author: Roland Junior Toussaint
# username: toussaintr
# Assignment: A5
# Purpose: To practice functions and gain practice with screen coordinates by
# creating a city scape.
#
######################################################################
# Acknowledgements:
#   Structured after code written by Dr. Jan Pearce
#   Pearce code copied from:
#   http://moodle2.berea.edu/pluginfile.php/143687/mod_resource/content/1/turtle-cityscape.py
######################################################################
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

#Create Sun
a.hideturtle()
a.penup()
a.home()                #Orients turtle back to (0,0)
a.setpos(200,180)       #sets sun location
a.color('yellow')       #sun color
a.pendown()
a.begin_fill()
a.circle(50) # Draws a circle of the indicated radius. Assuming the radius is positive, the circle is drawn tangent to the direction of myturtle in a clockwise direction.
a.end_fill()

def make_house(x, y, house_color, chimney_color, door_color, smoke_color):
    """ draw a house with the given colors and cordinates"""
    house=turtle.Turtle()
    house.penup()
    house.setpos(x,y)
    house.pendown()
    house.speed(0)
   #House
    house.pencolor(house_color) # Makes house outline black
    house.penup()
    house.setpos(x,y-20)     #Determines location on map
    house.pendown()
    #Chimney
    house.shape('square')
    house.shapesize(stretch_wid=22, stretch_len=2, outline=0)
    house.fillcolor(chimney_color)
    house.stamp()
    #Main building
    house.fillcolor(house_color)     #color of second circle
    house.shape('circle')           # makes igloo
    house.shapesize(stretch_wid=20, stretch_len=20, outline=0)
    house.stamp()
    #Door outline
    house.setpos(x,y+10)        #Sets door location
    house.color(house_color)
    house.pencolor(door_color)
    house.shape('circle')       #Creates border around door
    house.shapesize(stretch_wid=10, stretch_len=7, outline=0)
    house.stamp()
    #Create door
    house.setpos(x,y+10)        #sets door location
    house.color(door_color)
    house.shape('circle')#creates door
    house.shapesize(stretch_wid=8, stretch_len=5, outline=0)
    house.stamp()
    #Create ground for house
    house.setpos(x,y-150)       #creates ground
    house.color('forest green')
    house.shape('square')
    house.shapesize(stretch_wid=12, stretch_len=30, outline=0)
    house.stamp()
    #Create Smoke
    house.hideturtle()      #makes turtle invisible
    house.penup()
    house.setpos(x,y)       #sets location of smoke
    house.pensize(3)
    house.left(90)
    house.forward(200)      #Height above chimney smoke starts
    house.pendown()         #This is the code to get the turtle to top of the chimney
    house.color(smoke_color)
    house.right(180)
    house.forward(5)
    for i in range(7):      #Loops the circles that make the smoke
        house.right(50)
        house.forward(1)
        for i in range(20):
                house.forward(7)
                house.right(15)

    return house

for i in range (2):
    house=make_house(i*-100+160-i*310,i*1,'white','grey','black', 'black')


def make_flower(x, y, stem_color, flower_color, fill_color):
    """ draw a flower with the given colors and cordinates"""
    flower=turtle.Turtle()
    flower.hideturtle()
    flower.penup()
    flower.setpos(x,y)      #sets location of flower
    flower.pendown()
    flower.speed(0)
    # Make flower stem
    flower.pencolor(stem_color) #Sets the color of the stem
    flower.pensize(3)    #Thickness of flower
    flower.left(90)
    flower.forward(35)
    flower.left(90)
    flower.forward(5)
    flower.right(90)
    # Make flower
    flower.pencolor(flower_color)  # Color of outline of flower
    flower.fillcolor(fill_color)   # Internal color of flower
    flower.begin_fill()  # Fills the flower
    for i in range(7):   # Loop for the petals
        flower.left(120)
        for i in range(20):
            flower.forward(2)
            flower.left(15)
    flower.end_fill() # The figure drawn between the two fill commands is filled with the present color setting

    return flower


for i in range (2):
    flower=make_flower(-100, i*-100-120, 'green', 'pink', 'purple')
    flower=make_flower(200, i*-100-130, 'green', 'red', 'orange')
    flower=make_flower(-200, i*-150-125, 'green', 'orange', 'yellow')
    flower=make_flower(100, i*-160-120, 'green', 'hot pink', 'light blue')


wn.exitonclick()
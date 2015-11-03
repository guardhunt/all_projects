#-------------------------------------------------------------------------------
# Name:        fraction_writer.py
# Purpose: This module contains the functionality of the fraction_writer class
#   as well as other turtles to write out onto the screen the other parts of the
#   fraction statement. The fraction_writer object is only used to draw the
#   numerator, the bar, and the denominator.
#   The additional parts include the operator symbol, the equal sign, and the
#   "right" and "wrong" text that appears based on whether the user was able
#   to calculate the correct result.
#
# Author:   Mario Nakazawa
# Username: nakazawam
#
# Created:     Mar/30/2014
# ------------------------------------------------------------------------------

import turtle
class fraction_writer:
    '''This is an object that contains a Fraction and draws it to the
    screen. '''
    def __init__(self, x_coord=-100, y_coord=-100):
        '''intialize the positions of the fraction, moving its numerator
        and denominator turtles in position so that the number appears as
        needed.'''

        self.bar = turtle.Turtle()
        self.bar.hideturtle()
        self.bar.penup()
        self.bar.setpos(x_coord, y_coord)
        self.bar.pendown()
        self.bar.forward(100)

        self.numer_writer = turtle.Turtle()
        self.numer_writer.hideturtle()
        self.numer_writer.penup()
        self.numer_writer.setpos(x_coord+50, y_coord)

        self.denom_writer = turtle.Turtle()
        self.denom_writer.hideturtle()
        self.denom_writer.penup()
        self.denom_writer.setpos(x_coord+50, y_coord-60)


    def redraw_numerator(self, new_numer):
        '''a new numberator is redrawn to be the value new_numer. The
        denominator is not changed.'''
        self.numer_writer.clear()
        self.numer_writer.write(new_numer, False, "center",font=("Arial",40,("bold","normal")))

    def redraw_denominator( self, new_denom ):
        '''a new denominator is redrawn to be the value new_denom'''
        self.denom_writer.clear()
        self.denom_writer.write(new_denom, False, "center",font=("Arial",40,("bold","normal")))

    def redraw_fraction( self, input_fraction ):
        '''Given a fraction, it will update the numbers that it draws for the
        fraction it represents'''
        self.redraw_numerator( input_fraction.numerator )
        self.redraw_denominator( input_fraction.denominator )

#---------------------------------------------------------------------
#   When the user presses "a", "s", "d", "f", the number built so far
#   in the module class_fraction_window_listener gets assigned to the
#   numerator or denominator of the appropriate fraction.
#---------------------------------------------------------------------
def update_operator( new_symbol ):
    '''A function call to update the operator symbol between the two fraction_writers'''
    operator_turtle.write(new_symbol, False, "center",font=("Arial",40,("bold","normal")))

def output_correct():
    import time
    response_writer.color("blue")
    response_writer.write("RIGHT!", False, "center",font=("Arial",100,("bold","normal")))
    time.sleep(2)
    response_writer.clear()

def output_incorrect():
    import time
    response_writer.color("red")
    response_writer.write("WRONG!", False, "center",font=("Arial",100,("bold","normal")))
    time.sleep(2)
    response_writer.clear()

# Draw out the fraction statement
fraction_equation_y = -100
fraction_w1 = fraction_writer(-250,fraction_equation_y)
fraction_w2 = fraction_writer(-50,fraction_equation_y)
fraction_result_w = fraction_writer(150,fraction_equation_y)

# this turtle outputs either "wrong" or "right based on whether the user
# put the correct the sum of the two fractions.
response_writer = turtle.Turtle()
response_writer.hideturtle()
response_writer.penup()

# this turtle draws the operator because it is possible to expand this fraction
# statement to have multiplication or subtraction.
operator_turtle = turtle.Turtle()
operator_turtle.hideturtle()
operator_turtle.penup()
operator_turtle.setpos(-100,fraction_equation_y-30)
operator_turtle.write("+", False, "center",font=("Arial",40,("bold","normal")))

# this turtle just draws the equals sign. It has to be its own turtle because
# the others can change what they display, and calling clear() would erase
# EVERYTHING that it has drawn, which would erase the equal sign.
equal_sign = turtle.Turtle()
equal_sign.hideturtle()
equal_sign.penup()
equal_sign.setpos(100,fraction_equation_y-30)
equal_sign.write("=", True, "center",font=("Arial",40,("bold","normal")))

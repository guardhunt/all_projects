#-------------------------------------------------------------------------------
# Name:        fraction_class.py
# Purpose: A program that implements a fraction class to create these objects and
# usesthe turtle graphics for interactivity in the module "fraction_writer.py".
# - It uses the "fraction_window_listener.py" module to get numbers from the
#   user through the key-presses (0-9 for digits and the backspace to delete).
# - It uses fraction_writer.py" for functionality to write the fraction on the
#   screen using the turtle library.
#
#   The two functions
#       (1) add_the_fractions(fraction1, fraction2)
#       (2) check_sum_fractions()
#   are incomplete.
#   The method
#       (1) add_fraction( self, fraction_to_add )
#   is also incomplete.
#   All the functions have the appropriate docstrings defined for them.
#
# Author:   Mario Nakazawa
# Username: nakazawam
#
# Created:     Mar/30/2014
# ------------------------------------------------------------------------------

import turtle
import Tkinter
from fraction_window_listener import input_number   # this is the number built from the user
from fraction_window_listener import set_up_window  # this sets up the onkey functions
from fraction_writer import fraction_w1 # this is for the fraction drawing utility
from fraction_writer import fraction_w2 # this is for the fraction drawing utility
from fraction_writer import fraction_result_w # this is for the fraction drawing utility

win = turtle.Screen()
set_up_window(win)      # defined in fraction_window_listener.py module

#---------------------------------------------------------------------
#   CLASS DEFINITIONS
#---------------------------------------------------------------------
class Fraction:
    '''This class defines fractions with a numerator and denominator.
    It also has to methods to set the values of each of these parts
    explicitly'''
    def __init__( self, numer, denom ):
        self.numerator = numer
        self.denominator = denom

    def set_numerator( self, new_numer ):
        self.numerator = new_numer

    def set_denominator( self, new_denom ):
        self.denominator = new_denom

    def reduce_fraction( self ):
        '''This method reduces the fraction using Euclid's algorithm, which is:
            "Starting with a pair of positive integers, form a new pair
            consisting of the smaller number and the difference between
            the larger number and the smaller number.
            This process repeats until the numbers in the new pair are
            equal to each other; that value is the greatest common divisor
            of the original pair." (from http://en.wikipedia.org/wiki/Euclidean_algorithm)
        For example, suppose the fraction is 56/140. Picking the smaller of
        the two and subtracting it from the larger number, we generate the pair
        (56, 84) because 140 - 56 = 84. Repeating that process, we get
        (56, 28) because 84 - 56 = 28. Now 28 is the smaller number, so we
        subtract that from 56 (the larger number) and the pair becomes (28, 28).
        Both numbers are the same, so we conclude that 28 is the greatest common
        factor, which it is! Dividing numerator and denominator by 28,
        56/140 = 2/5.'''

        # Start with the assumption that the numerator is smaller than the
        # denominator and then fix it if necessary.
        smaller = self.numerator
        bigger = self.denominator
        if( bigger < smaller ):
            switch = bigger
            bigger = smaller
            smaller = switch

        # start the loop to find the greatest common factor
        # remember, we need to keep going until they are the same.
        while( bigger != smaller ):
            bigger = bigger - smaller   # calculate the difference
            if( bigger < smaller ):     # switch if necessary
                switch = bigger
                bigger = smaller
                smaller = switch

        # now that we have the greatest common factor, divide both
        # numerator and denominator with it.
        self.numerator = self.numerator / bigger
        self.denominator = self.denominator / bigger

    def add_fraction( self, fraction_to_add ):
        '''Given a Fraction object as input, add it to itself so that it
        becomes the sum of what it had and what was input.
        For example, if this Fraction was equal to 1/5 (numerator is 1 and
        denominator is 5) and a Fraction object that has the value of 1/2
        (numerator is 1 and denoninator is 2) is passed in, this object would
        become 7/10 (numerator is 7 and denominator is 10).'''
        if self.denominator != fraction_to_add.denominator:
            den = self.denominator * fraction_to_add.denominator
            num1 = self.numerator * fraction_to_add.denominator
            print num1
            num2 = fraction_to_add.numerator * self.denominator
            print num2
            self =((num1 + num2), den)
        elif self.denominator == fraction_to_add.denominator:
            den = self.denominator
            num = self.numerator + fraction_to_add.numerator
            self = (num, den)
        return self

        # fix me!

#---------------------------------------------------------------------
#   CALCULATIONS
#---------------------------------------------------------------------
def add_the_fractions(fraction1, fraction2):
    '''This fruitful function takes two Fraction objects as input, adds
    them together and returns the sum.
    One way to do this is to create a result Fraction object that is first
    set to be the same as fraction1, and then call its add_fraction() method
    to add fraction2 to it.'''
    result = fraction1.add_fraction(fraction2)
    #result = Fraction( 1,1 ) #fix me!!
    return result

def display_instructions():
    '''Display the instructions for the program.'''
    input_x = -300
    input_y = 20
    instructions = '''Welcome! Try to guess the sum of two fractions
    You can press 'q' at any time to quit.
    Press digit keys to build numbers/backspace to delete numbers
    To assign the number you have created so far, press:

        'a' to set it to the result fraction numerator
        'z' to set it to the result fraction denominator

    You can quit by pressing 'q' at any time, and
                             '+' to check if your sum is correct.'''
    instruction_turtle = turtle.Turtle()
    instruction_turtle.hideturtle()
    instruction_turtle.penup()
    instruction_turtle.setpos(input_x,input_y)
    instruction_turtle.write(instructions, False, "left",font=("Arial",15,("normal","normal")))
    instruction_turtle.setpos(input_x+300,input_y-55)
    instruction_turtle.write("Input Number:", False, "left",font=("Arial",20,("bold","normal")))

def check_sum_fractions():
    '''Takes the two fractions that are displayed to the screen but are actually
    stored in the objects fraction1 and fraction2 and adds them together.
    It then takes that sum and compares it with what the user entered
    (stored in fraction_result). It then writes CORRECT or WRONG! across the
    screen based whether the user was right or, well, wrong..'''
    pass # fix me!

#---------------------------------------------------------------------
#   EVENT HANDLERS
#   Set up everything for interaction with the user.
#---------------------------------------------------------------------
win.onkey(win.bye,"q")
win.onkey(check_sum_fractions,"+")

#---------------------------------------------------------------------
#   When the user presses "a", "z", the number built so far
#   in the module fraction_window_listener gets assigned to the
#   numerator or denominator of the resulting fraction. These
#   functions are in the fraction_writer module.
#---------------------------------------------------------------------
def result_numerator():
    '''Take the number built in the input_number object and set the
    numerator for the first fraction to it.'''
    fraction_result.numerator = int(input_number.number_string)
    fraction_result_w.redraw_fraction(fraction_result)

def result_denominator():
    '''Take the number built in the input_number object and set the
    denominator for the first fraction to it.'''
    fraction_result.denominator = int(input_number.number_string)
    fraction_result_w.redraw_fraction(fraction_result)

win.onkey(result_numerator,"a")
win.onkey(result_denominator,"z")

win.listen()

display_instructions()

#-------------------------------------------------------------------
# CREATE THE FRACTIONS THAT ARE TO BE ADDED TOGETHER
#-------------------------------------------------------------------
import random
fraction1 = Fraction(random.randint(1,20),random.randint(1,20))
fraction2 = Fraction(random.randint(1,20),random.randint(1,20))

print( fraction1.numerator, fraction1.denominator )
print( fraction2 )
print ( fraction2.numerator, fraction2.denominator )


fraction1.reduce_fraction()
fraction2.reduce_fraction()
print add_the_fractions(fraction1, fraction2)

# Have the default result be 1/1
fraction_result = Fraction(1,1)

#--------------------------------------------------------------------
# Draw the fractions on the screen using the objects
#   fraction_w1
#   fraction_w2
#   fraction_result_w
#--------------------------------------------------------------------
fraction_w1.redraw_fraction(fraction1)
fraction_w2.redraw_fraction(fraction2)
fraction_result_w.redraw_fraction(fraction_result)

Tkinter.mainloop()
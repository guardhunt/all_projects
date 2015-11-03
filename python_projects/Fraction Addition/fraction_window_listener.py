#-------------------------------------------------------------------------------
# Name:        fraction_window_listener.py
# Purpose: This module handles all the keystroke listening for the digits of the
#   number input into the vairable called input_number.
#   This object enables backspace deletions.
#
# Author:   Mario Nakazawa
# Username: nakazawam
#
# Created:     Mar/30/2014
# ------------------------------------------------------------------------------

import turtle

class Input_Number:
    def __init__( self, x_pos=-120, y_pos=0 ):
        self.number_string = ""      # this is the string that will be the built number
        # we will introduce a turtle that we will use to display the number the
        # user typed in so far on the screen
        self.input_number_turtle = turtle.Turtle()
        self.input_number_turtle.hideturtle()
        self.input_number_turtle.penup()
        self.input_number_turtle.setpos( x_pos, y_pos )
        self.input_number_turtle.write(self.number_string, False, "left",font=("Arial",30,("bold","normal")))

    def update_turtle(self):
        '''When digits are being added to the string, it appears on the screen
        when this turtle object is updated.'''
        self.input_number_turtle.clear()
        self.input_number_turtle.write(self.number_string, move=False, font=("Arial",30,("bold","normal")))
    #---------------------------------------------------------------------
    #   These next functions "BUILDS" the numbers input from the keyboard
    #   into a attribute called "number_string".
    #   The object allows user needs to type a period (".") to get clear the
    #   number string, and it records all the digits the user inputs.
    #---------------------------------------------------------------------
    def clear_number( self ):
        '''Clear the number_string'''
        self.number_string = ""
        self.input_number_turtle.clear()
    def delete_digit( self ):
        '''This method catches the backspace key and removes the last digit in
        the string it is building.'''
        new_string = ""
        index=0
        while(index < len(self.number_string)-1):
            new_string += self.number_string[index]
            index = index + 1
        self.number_string = new_string
        self.update_turtle()

    def add_zero( self ):
        self.number_string += "0"
        self.update_turtle()
    def add_one( self ):
        self.number_string += "1"
        self.update_turtle()
    def add_two( self ):
        self.number_string += "2"
        self.update_turtle()
    def add_three( self ):
        self.number_string += "3"
        self.update_turtle()
    def add_four( self ):
        self.number_string += "4"
        self.update_turtle()
    def add_five( self ):
        self.number_string += "5"
        self.update_turtle()
    def add_six( self ):
        self.number_string += "6"
        self.update_turtle()
    def add_seven( self ):
        self.number_string += "7"
        self.update_turtle()
    def add_eight( self ):
        self.number_string += "8"
        self.update_turtle()
    def add_nine( self ):
        self.number_string += "9"
        self.update_turtle()
# Put the input_number object to the right of the center because that is
# where we want to see the number being built.
input_number = Input_Number(180,-40)

def clear_number():
    input_number.clear_number()
def delete_a_digit():
    input_number.delete_digit()
def get_zer():
    input_number.add_zero()
def get_one():
    input_number.add_one()
def get_two():
    input_number.add_two()
def get_thr():
    input_number.add_three()
def get_fou():
    input_number.add_four()
def get_fiv():
    input_number.add_five()
def get_six():
    input_number.add_six()
def get_sev():
    input_number.add_seven()
def get_eig():
    input_number.add_eight()
def get_nin():
    input_number.add_nine()

def set_up_window( win ):
    '''This function sets up the window to listen for digits and builds the
    string of the number as the user types the digits. The period resets the
    string to blank.'''
    win.onkey(clear_number, '.')
    win.onkey(delete_a_digit, "BackSpace")
    win.onkey(get_zer, '0')
    win.onkey(get_one, '1')
    win.onkey(get_two, '2')
    win.onkey(get_thr, '3')
    win.onkey(get_fou, '4')
    win.onkey(get_fiv, '5')
    win.onkey(get_six, '6')
    win.onkey(get_sev, '7')
    win.onkey(get_eig, '8')
    win.onkey(get_nin, '9')

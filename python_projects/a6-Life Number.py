#-------------------------------------------------------------------------------
# Author: Roland Junior Toussaint
# username: toussaintr
#
# Assignment: A6
# Purpose: demonstration of the use of fruitful function and return values.
######################################################################
# Acknowledgements:
#   http://seventhlifepath.com/.
######################################################################
#-------------------------------------------------------------------------------
#Imports from library
import turtle
import random

#Asks for the first to digits of month
firstinput=raw_input('Please put your two digit birth month [ex: 04 for April]')

month= firstinput   #Assigns name month to user input

def month_number(amount):   #This funtion calculates month number
    """This function takes the raw input of two digits that the user
    gives and splits it into two intergers. Then it adds them together
    and outputs users month life number."""
    for i in (month):

        if firstinput == str(11):   #if input is 11
            return int(11)
        else:
            unit_one=int (month [:1])
            unit_two=int (month [1:2])
            return int(unit_one + unit_two)

#Day input asks for two digit day of birth
secondinput=raw_input('Please put the day you were born [ex: 22]')

day= secondinput #Assigns name day to user input

def day_number(amount): #This funtion calculates day number
    """This function takes the raw input of two digits that the user
        gives and splits it into two intergers. Then it adds them together
        and outputs users day life number."""
    for i in (day):

        if secondinput == str(11):  #if the number is 11
            return int(11)
        elif secondinput == str(22):    #if the nmber is 22
            return int(22)
        else:                       #if the number is two digits
            unit_one=int (day [:1])
            unit_two=int (day [1:2])
            return int(unit_one+unit_two)

#Year input asks for four digit year of birth
thirdinput=raw_input('Please put the year you were born [ex: 1993]')

year= thirdinput    #Assigns name year to user input

def year_number(amount): #This function calculates year number
    """This function takes the raw input of four digits that the user
        gives and splits it into two intergers. Then it adds them together
        and outputs users year life number."""
    for i in (year):
        unit_one=int (year [:1])
        unit_two=int (year [1:2])
        unit_three=int (year [2:3])
        unit_four=int (year [3:4])
        return int(unit_one+unit_two+unit_three+unit_four)

#Assign name to total of first three funtions
sum_of_life = (month_number(month)+day_number(day)+year_number(year))

#Converts the total intreger to a string
total= str(sum_of_life)

def final_number(amount): #This creates the function to simplify number
    """This function takes the sum total of the previous three functions
    and if the total is not 11, 22 or 33 then it simplifys it to one unit"""
    for i in (total):
        if sum_of_life == int(11):
            return str(11)
        elif sum_of_life == int(22):
            return str(22)
        elif sum_of_life == int(33):
            return str (33)
        else:
             unit_one=int (total [:1])
             unit_two=int (total [1:2])
             return int (unit_one+unit_two)

#This turns the result from the function into a string
endresult = str (final_number(total))

def final_calculation (amount):
    """This function simplifies the total form final_number if the total is
     10 or a 12. It would then split them into idividual digits and add
     together. If it is not 10 or 12 it return the original number entered"""
    for i in (endresult):
        if endresult == str(11):
            return int(11)
        elif endresult == str(10):
            unit_one = int(endresult[:1])
            unit_two = int(endresult[1:2])

            return int(unit_one+unit_two)
        elif endresult == str(12):
            unit_one = int(endresult[:1])
            unit_two = int(endresult[1:2])

            return int(unit_one+unit_two)
        else:
            return endresult

#############################################################

#This prints your life number on a screen
print 'Your life number is...'
#This sets up the turtle screen and position
wn = turtle.Screen()
number = turtle.Turtle()
number.up()
number.setpos(-20,-400)
number.hideturtle()

#Shows the life number and loops random flashing colors, in
#papyrus font.
for i in range(2000):
    number.color(random.random(),random.random(), random.random())
    wn.bgcolor(random.random(),random.random(), random.random())
    number.write(str(final_calculation(endresult)),move=False,align='center',font=("Papyrus",400,("bold","italic")))


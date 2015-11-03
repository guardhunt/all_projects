######################################################################
# Modified by: Roland Junior Toussaint
#
######################################################################
# A flawed programwhich uses a funciton to determine the area of a circle

# Author: Jan Pearce
# username: pearcej
#
# Background:
# The area of a circle is the number of square units inside that circle.
# a formula for this area is a = PI * r**2 where PI is an irrational number
# opproximated by PI=3.141592

# Purpose
# To learn to debug programs with flow-of control and parameter passing problems
# There are several problems.
######################################################################
# Acknowledgements:
    # This is original BAD code
######################################################################
# Function
def circleArea(r): # kept r as the variable
    """takes user input, squares it and then multiplies it by PI, returning the
       area of the circle"""
    PI = 3.141592
    #removed the i = r i did nothing
    area = PI * int(r)**2 # changed the r into an integer so the formula works
    return area

#######################################################################
# This is where the main program starts

r = raw_input('please enter desired radius: ') # Set r equal to the raw_input, so r = what the user gives
myarea=circleArea(r)
print(myarea)
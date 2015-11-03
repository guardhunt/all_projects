######################################################################
# Author: Roland Junior Toussaint
# Assignment: A0
# Purpose: To test out the installation of python and pyscripter
# and to play around with a few features of the python language.
#
#
######################################################################
# Acknowledgements:
#   This program agnoligizes the only great color blue
#   facts from http://www.realclearscience.com/blog/2012/04/blue%20is%20the%20best.html

# You need to acknowledge having modifed this code and all other code you modify
# or use for assitance.
#   To do so, you will indicate something like:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://faculty.berea.edu/pearcej/csc226/tasks/yourusername-A0.py
######################################################################

import time          # import a library with time.sleep()
import random        # import a library with random.choice()

# This is how to ask for input from the keyboard:
myname = raw_input('What is your favorite color?')

print('') # This prints a blank line.

#This is a python conditional statement


if myname == 'Blue' or 'blue': # else if
    print('You picked the only decent color ' + myname + '!')
    print('All other colors are terrible in contrast')
    time.sleep(2)
    print('I approve of you as a human')
if myname == 'red' or myname == 'Red' or myname == 'Green' or myname=='green':
    print('Wow you picked ' + myname + '. That is an aweful color!')

# The following are from http://www.realclearscience.com/blog/2012/04/blue%20is%20the%20best.html
saying1='Blue light travels the farthest through water'
saying2='Blue light may help with depression'
saying3='Blue light makes better movies'
saying4='Blue light helps plants grow'
saying5='Blue light is everyones favorite'
saying6='Juniors favorite color is blue'
somechoice = random.choice([saying1,saying2,saying3, saying4, saying5, saying6])

time.sleep(0.5)
print('')
print('In fact, here is a reason you should have picked blue')
print(somechoice)

# Be sure to change the filename of this file to your username-a0.py
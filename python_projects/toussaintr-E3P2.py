#-------------------------------------------------------------------------------
# Name:       csc226E3-part2.py
# Purpose: A program that implements the automobile class, which has one
#   state variable, gear_state
#
# Created:     Apr/16/2014
# ------------------------------------------------------------------------------
# Exam E3 Part 2
# Instructions:
#   (9 points)
#   Implement the two functions shift_up() and shift_down(), which change the
#   state of the Automobile so that its gear_state goes up and down by one,
#   respectively. Make sure you prevent cases such as when you try to shift-up
#   beyond its max gear or shift down below its minimum.
#   NOTHING SHOULD BE OUTPUT TO THE SCREEN!
#   Make sure to insert appropriate docstrings and comments, they are worth points.
#
#   (6 points)
#   Complete the function test_Automobile_class() that creates an Automobile
#   object and tests whether the methods you implemented in part 1 work. Make sure
#   you test for cases such as when you try to shift-up beyond its max gear or
#   shift down below its minimum, and this function should output to the screen
#   what gear the Automobile object is in using the appropriate method of the
#   Automobile class.
#
#-------------------------------------------------------------------------------
#
# Your Name:  Roland Junior Toussaint
#
class Automobile:
    def __init__(self):
        self.gear_state = 0 # set to neutral

# ##########################################################################
# PART 1:
#   Complete the two methods shift_up() and shift_down()
# ##########################################################################
    #########################
    # define the shift_up() function below, where each time it is called,
    # the gear is increased by one. This gear cannot go above 5, so once
    # it reaches 5, it stays there when this method is called.
    #########################
    def shift_up(self):
        '''Increases the autos gear by 1 if it is not in the 5 gear'''
        if self.gear_state < 5: # If the gear is less than gear 5 run
            self.gear_state += 1 # Adds one to the gear state


    #########################
    # define the shift_down() function below, where each time this method
    # is called, the gear_state decreases by one. This gear cannot go below
    # -2 (which is the fastest the automobile can go in reverse). Once the
    # gear reaches -2, it stays there if this method is called.
    #########################
    def shift_down(self):
        '''Decreases the autos gear by 1 if it is not in the -2 gear'''
        if self.gear_state > -2: # If the number is larger than -2
            self.gear_state -= 1 # Removes one from gear state.


    def to_string(self):
        return "Auto is in {0} gear.".format(self.gear_state)
# ##########################################################################
# PART 2:
#   Complete the following function which TESTS the Automobile class.
#   Make sure to test for multiple gear shifts upwards and downwards. This
#   function should output to the screen what gear the Automobile object is
#   in using the appropriate method of the Automobile class.
# ##########################################################################
def test_Automobile_class():
    '''This function creates an object of type Automobile and tests whether
    the shift_up() and shift_down() methods of that class work.'''
    car = Automobile
    for i in range(6): # Creates a loop to test if car will shift above gear 5
       car.shift_up() # Calls shift_up module
    print car.to_string() # Print what gear auto is in should be 5
    for i in range(8): # Creates loop to test if car will shift bellow -2
        car.shift_down() # Calls shift down module
    print car.to_string() # Prints gear auto is in should be -2


test_Automobile_class() # This calls the test automibile class function
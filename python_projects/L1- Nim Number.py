#-------------------------------------------------------------------------------
# Author: Roland Junior Toussaint
# username: toussaintr
#
# Assignment: L1
# Purpose: Practice breaking a larger problem down into smaller "pieces"using
# functions, Gain practice using loops and modulus, Practice debugging.
######################################################################
# Acknowledgements:
#
#   The game is from http://education.jlab.org/nim/s_index.html, and is called
#   the Nim Number Game
######################################################################
#------------------------------------------------------------------------
import math
import random
import time
##############################################################################
# Functions
def computer_choice(number):
        """determines how many the computer will remove, and will create a loop
        allowing it to win if the original number is not a divisible of 5"""
        if number <= 4: # if the number is 4 or less win game
            return number
        elif number % 5 == 0: # if divisible take a random number between 1-4
            a = 1
            b = 2
            c = 3
            d = 4
            number = random.choice([a,b,c,d])   # this randomally selects number
            return number
        else:
            take = number % 5   # if not divisible by 5 take remainder
            number = take
            return number
##############################################################################


number = raw_input('How many balls would you like to start the game? Please pick any number 15 or higher?')
number = int(number)    # this turns the raw_input from str to int
while (number <= 14):   # this loop requests a new input till raw_input is <15
    number = int(raw_input('Thats not enough please pick a higher number.'))
print('Alright then lets play the game.')

print ("You play first")


while number > 0:   # this while loop runs until mumber is equal to 0
    number = str(number)    # turns the number into a str
    # this asks for the number of balls the user would like to take
    second_input = raw_input ('How many would you like to take, there are '+ number +' balls left?')
    print ('')
    print ('You decided to take '+ str(second_input)+' balls.') #tells them how many balls they took
    second_input = int(second_input)    # turns user input into an int
    number = int(number)    # turns number of balls back to int

    if second_input > 4:    # runs if input is larger than 4
        print ('That is not a number please select between 1-4')

    elif second_input == 0: # runs if input is 0
        print ('That is not a number please select between 1-4')

    elif second_input <= 4: # runs if number is between 1-4
        players_pick = int(second_input)
        number = number - players_pick  #takes original number and removes input_2

        if number == 0: # runs if new total is 0
            print ('Congradulations you win!')

        elif number != 0:   # runs if number is not equal to 0
            time.sleep(1.0)
            if computer_choice(number) < 5: # calls function
                computer = computer_choice(number)  # renames output so it can print
                number = number - computer  # removes the computers number of balls
                print ('')
                print ('The computer takes '+ str(computer) + ' balls.')    # tells user how many balls are taken
            time.sleep(1.0)
            if number != 0: # tells user how many balls remain
                print ('')
                print (str(number) + ' balls remain.')
                number = int(number)
            if number == 0: # tells if the computer wins the game
                print ('Computer wins!')




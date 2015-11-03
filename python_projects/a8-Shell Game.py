
#-------------------------------------------------------------------------------
# Author: Roland Junior Toussaint
#
# username: toussaintr
#
# Assignment: A8
#
# Purpose: Develop a program to play the shell game and Practice useing
# functions for encapsulation, practice loops, and fruitful functions
######################################################################

#funtions
def start_amount():
    """This function asks for an input from the user on the amount of money they
    want to start betting with. If number is lower than 0 or greater than 1000
    it prompts user for new input, until it is within the perameters. Returns
    the users input"""
    start_money = int(raw_input('How much money do have to gamble with?')) #Asks for start amount
    while start_money < 0 or start_money > 1000: # sets parameter user can only enter between 0-1000
        print 'Sorry this is low scale gambling, we cannot handle more than $1000' # Loop prevents user from taking more than 1000
        start_money = int(raw_input('How much money would you like to gamble with?'))
    return int(start_money) # returns the users inputed money

def shell_randomizer():
    """This selects a random shell for the ball to be under, by returning either
    left, middle or right"""
    shell1 = 'left'
    shell2 = 'middle'
    shell3 = 'right'
    correct_shell = random.choice([shell1, shell2, shell3])
    return correct_shell

def amount_bet(new_total):
    """ Takes a user input to determine how much they would like to bet, and
    determines if it is valid by checking it against the parameter new_total.
    It returns the amount bet."""
    bet = int(raw_input('How much do you want to bet this round?'))
    while bet > new_total: # Checks if they have enough money to bet
        bet = int(raw_input('You only have $' + str(new_total) +'. How much do you want to bet?'))
    while bet <= 0: # prevents user from betting 0 or less
        bet = int(raw_input('Sorry this is gambling, you need to bet somthing. What do you want to bet?'))
    print 'You bet $' + str(bet) # shows player amound they bid
    return bet

def check_guess(correct_shell, new_total, bet):
    """takes the output of correct shell and checks if it matches the user input.
    then it either adds or subtracts the amount bet from new_total. It then returns
    the value for new_total"""
    selection = raw_input('What shell is the ball under? The left, right, or middle one?')
    if selection == correct_shell: # this runs if user input matches random shell
        print 'Congradulations you were correct, you made $' + str(bet)
        new_total = new_total + bet # Adds bet to total
    elif selection != correct_shell: # Runs if the input does not match random shell
        print'Sorry it was under the ' + correct_shell + ' shell, you lost $' + str(bet)
        new_total = new_total - bet # Subtracts bet from total

    print 'You now have $' + str(new_total)
    return new_total

#-------------------------------------------------------------------------------
#Imports from library
import random

new_total = start_amount() #Sets new_total to the output int of start_amount

times_played = 0 # Sets the times played to 0 so it can count up to ten

while new_total > 0: # This loop runs as long the user has more than $0
    if times_played < 10: # Conditional statement that it loops 10 times, then breaks loop

        bet = amount_bet(new_total) # Sets return form amount_bet to bet

        correct_shell = shell_randomizer() # Sets shell_randomizer to correct_Shell

        new_total = check_guess(correct_shell, new_total, bet) # Sets the new_total to the check_guess funtion

        times_played += 1 #Counts the amount of times loop has run

    elif times_played == 10: # Once run 10 times it makes the new_total a negative number
        new_total *= -1 # Makes Neg breaking the while loop


if new_total < 0: # runs if the user played 10 rounds
    new_total *= -1 # Multiplies by -1 to make positive again
    print 'You used your 10 turns you ended with $' + str(new_total)
elif new_total == 0: # runs if user is out of money
    print 'Sorry you have no more money, better luck next time'
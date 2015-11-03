######################################################################
# Modified by Roland Junior Toussaint
# username: toussaintr
#
# Assignment: A3
# Purpose: To practice with loops and turtles
#######################################################################


import time          # import a library with time.sleep()
import random        # import a library with random.choice()

# This is how to ask for input from the keyboard:
myinput = raw_input('Rock, Paper, Scissors, Lizard, Spock')

print('You played ' + myinput + '!')

print('') # This prints a blank line.

saying1='Rock'
saying2='Paper'
saying3='Scissors'
saying4='Lizard'
saying5='Spock'

somechoice = random.choice([saying1,saying2,saying3, saying4, saying5])

time.sleep(0.5)
print('I played ' + somechoice + '!')

if myinput == 'Rock' or myinput == 'rock':
    if somechoice == 'Rock':
        print('Rock just hang out as buds, it is a tie!')
    if somechoice == 'Paper':
        print('Paper covers rock, I win!')
    if somechoice == 'Scissors':
        print ('Rock crushes scissors, you win!')
    if somechoice == 'Lizard':
        print('Rock crushes lizard, you win!')
    if somechoice == 'Spock':
        print('Spock varporizes rock, I win!')
elif myinput == 'Paper' or myinput == 'paper':
    if somechoice == 'Rock':
        print('Paper covers rock, you win!')
    if somechoice == 'Paper':
        print('Paper just lays there and does nothing, it is a tie!')
    if somechoice == 'Scissors':
        print('Scissors cuts paper, I win!')
    if somechoice == 'Lizard':
        print('Lizard eats paper, I win!')
    if somechoice == 'Spock':
        print('Paper disproves Spock, you win')
elif myinput == 'Scissors' or myinput == 'scissors':
    if somechoice == 'Rock':
        print('Rock crushes scissors, I win!')
    if somechoice == 'Paper':
        print('Scissors cut paper, you win!')
    if somechoice == 'Scissors':
        print('Scissors hang out as bros, it is a tie!')
    if somechoice == 'Lizard':
        print('Scissors decapitate lizard, you win!')
    if somechoice == 'Spock':
        print('Spock breaks scissors, I win!')
elif myinput == 'Lizard' or myinput == 'lizard':
    if somechoice == 'Rock':
        print('Rock crushes lizard, I win!')
    if somechoice == 'Paper':
        print('Lizard eats paper, you win!')
    if somechoice == 'Scissors':
        print('Scissors decapitate lizard, I win!')
    if somechoice == 'Lizard':
        print('Lizards stares blankly at each other, it is a tie!')
    if somechoice == 'Spock':
        print('Lizard poisons Spock, you win!')
elif myinput == 'Spock' or myinput == 'spock':
    if somechoice == 'Rock':
        print('Spock vaporizes rock, you win!')
    if somechoice == 'Paper':
        print('Paper disproves Spock, I win!')
    if somechoice == 'Scissors':
        print('Spock breaks scissors, you win!')
    if somechoice == 'Lizard':
        print('Lizard poisons Spock, I win!')
    if somechoice == 'Spock':
        print('Spock meets himself they both agree fighting is illogical, it is a tie!')
elif myinput == 'Darth Vader':
    print('Darth Vader destroys ' + somechoice + '! Nothing can defeat him, he is a Sith Lord!')
else:
    print('Wow, ' + myinput + '! You are dumber then I thought, I win automatically!')
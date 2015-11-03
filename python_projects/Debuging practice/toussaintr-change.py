######################################################################
# Modified by: Roland Junior Toussaint

######################################################################
# Purpose: This program has a bunch of problems with that need to be
#   fixed. It should be simple enough to be able to trace using the
#   debugger and find out what is wrong.
#   It is supposed to make change. After it asks the user for the
#   amount of money in cents, it outputs the number of quarters, dimes,
#   nickels and pennies needed to make the change.
#
# A SAMPLE RUN OF THIS PROGRAM with 34 CENTS OUTPUTS:
#   You need 1 coins worth 25 cents.
#   You need 0 coins worth 10 cents.
#   You need 1 coins worth 5 cents.
#   You need 4 coins worth 1 cents.
#
# MODIFIED: February 5, 2014
#  - simplified the code by taking out extra things that are not related
#    to the errors.
#  - added comments to explain what this program is doing
######################################################################
# Acknowledgements:
# A flawed change making program
#
# Author: Mario Nakazawa
# username: nakazawam
#
######################################################################
response = 'no'  # This start program without prompting user

# removed response equal no
if response != "yes" or response != "Yes":   # added the response == for second yes and changed to Yes the != made this and if
    while response == "no" or response == "No": 	# Made this a while statement to loop it, and added response == so it looks for No

        change = int(raw_input("How much money do we have to making change? "))

		# now that we are continuing, let's make some change!
        while( change <= 0 ): # Made this a while loop
			# Check to make sure that we are putting in a valid number. We cannot make
			# change on a negative number.
            change = int(raw_input("Can I have a postive number?")) #Made it ask for new number

        else:
            # Ok, output the number of each coin needed to make change
			# starting with the quarters, dimes, nickels and then pennies
            for coin in [25, 10, 5, 1]:
                num_coins = change // coin	# find the number of each type of coin
                change = change % coin		# find out how much is left after taking out
											# this change.
                # put the print into loop, so it would show change made
                print( 'You need '+ str(num_coins) + ' coins worth ' + str(coin) + ' cents.' )
        response = raw_input("Are we done?")	#pur this in while statement so it prompts user after first run




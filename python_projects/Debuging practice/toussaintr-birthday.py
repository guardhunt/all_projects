#####################################################################
# Modified by: Roland Junior Toussaint
#
######################################################################
# A flawed birthday program
#
# Author: Jan Pearce
# username: pearcej
#
# Purpose: This program has flow of control and parameter-passing
#           problems which need to be fixed.
######################################################################
# Acknowledgements:
    # This is original BAD code
######################################################################

def happyBirthday(name, number_times): # specified the the variables to be more specific
    """Takes the users assigned name to print into the Happy Birthday song,
        and the user assigned number_times they want the song to be printed"""  # Created a proper docstring

    for i in range(number_times): # changed to number_times
        print("Happy Birthday to you!") # added two Happy Birthdays at the top to make it the song
        print("Happy Birthday to you!")
        print("Happy Birthday, dear " + name + ".") # Changed the variable to i and assigned name since i is the in range of
        print("Happy Birthday to you!...") # Tabbed over the print into the function, or it would print once on its own

happyBirthday('Ivy', 2) # name and number of times to loop
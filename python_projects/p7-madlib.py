#-------------------------------------------------------------------------------
# Author: Roland Junior Toussaint
#
# Assignment: P7
# Purpose: Creates a madlib and practices string major, combines index, and
#           practices functions.
#-------------------------------------------------------------------------------
def create_madlib (adjective, place, animal, second_adjective, adverb, verb, relative, season):
    """This function creates the madlib from all of the rawinputs that are imported as parameters
    then returns the completed madlib"""
    madlib = '''This {7} I went to the {0} {1}. I rode a(n) {0} {2}, and had a {3} time!
    I {4} {5} my favorite {6}, it was {3}! My {6} is super flexible and {0}. I really love {6}
    I cannot wait to come back next {7}!'''.format(adjective, place, animal, second_adjective, adverb, verb, relative, season)
    return madlib
#-------------------------------------------------------------------------------

# These are the raw inputs that the string will select from
adjective = raw_input('Please provide an adjective')
place = raw_input('Please provide a location')
animal = raw_input('Please provide an animal')
second_adjective = raw_input('Please provide another adjective')
adverb = raw_input('Please provie an adverb')
verb = raw_input('Please provide a verb ending in -ed')
relative = raw_input('Please provide favorite relative')
season = raw_input('Please provide a season')

#Calls the function and prints result
print create_madlib(adjective, place, animal, second_adjective, adverb, verb, relative, season)

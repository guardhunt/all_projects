#-------------------------------------------------------------------------------
#
# Author:      Roland Junior Toussaint
#
# Created:     16/02/2014
# Copyright:   (c) toussaintr 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

tt = "Milk Tastes Delicious" # Prints in upperground
xx = tt.upper()
print xx

aa = xx[2]  # Prints third letter from front
print aa

aa = xx[-2] # Print second letter from back
print aa

bb = len(xx) # Prints number of characters
print bb

cc = 0 # Prints our idividual letters
while cc < len(xx):
    letter = xx[cc]
    print letter
    cc += 1

for c in xx: # Prints our idividual letters
    print (c)

word = raw_input('Give me a word')
if word < "Kanye":
    print("Your word, " + word + ", comes before Kanye.")
elif word > "Kanye":
    print("Your word, " + word + ", comes after Kanye")
else:
    print("Yes, we have no bananas!")

insult = 'dork'
name = 'weirdo'
s = "Damn son you a big {0} and a {1}".format(insult, name)
print s

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 3):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))

if 'apple' < 'pinapple':
    print 'True'
if '101' < '503':
    print 'True'
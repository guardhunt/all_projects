#-------------------------------------------------------------------------------
#
# Author:      Roland Junior Toussaint
#
# Created:     16/03/2014
# Copyright:   (c) toussaintr 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num_list = [6, 9, 69]
iam = ['God', 'Damn', 'Right']
kye = ['My', 2.3, iam]

print (num_list, iam, kye)

for i in [0, 1, 2]: # list transversal
    print kye[i]

print ''
for k in iam: # another way to do list transversal
    print (k)

print ''
for i in range(len(kye)):
    print (num_list[i])

print ''
print 'God' in iam
print 'God' in kye
print 'God' not in kye

print ''
cars = [
    ('Kye', ['Honda', 'Ford', 'Toyota']),
    ('Ivy', ['Honda', 'Toyota', 'Porche']),
    ('Robin', ['Ford', 'Toyota', 'Kia']),
    ('Gabby', ['Honda', 'Mercedes', 'Toyota', 'Kia'])]
count = 0
for (name, brands) in cars:
    if 'Honda' in brands:
        count += 1

print (str(count) + ' people want a Honda')
print ''

c = num_list + iam
print c

print ''
print num_list [2] * 4
print iam [2] * 4

print ''
print iam [1:2]
print iam [:3]

print ''  # this is called Item Assinment because lists are mutable
# Updating list values
iam[0] = 'No'
iam[1] = 'I dont know'
print iam[:]
# Adding items to list
iam[2:2] = "1" # This is odd
iam[2:2] = '2'
print iam
# Remove items to list
iam[1:2] = []
print iam

# Delete from list with Python
del kye[1]
print kye

print ''
# Strings store as same thing
a = 'Yay'
b = 'Yay'
print a is b
# lists do not
c = [1,2,3]
d = [1,2,3]
print c is d
# but this makes it true
c = d
print c is d #this is called Aliased changes made to one affects other
c[1] = 'a'
print d
# Cloning
f = iam[:]
print f

print ''
number = 1234
for number in range(20):
    if number % 3 == 0:
        print(number)

print ''
xs = [1, 2, 3, 4, 5]
for (i, val) in enumerate(xs): # same as for i in range len(xs)
    xs[i] = val**2
print xs
print ''

mylist = [5, 27, 3, 12]
mylist.insert(1, 12) # Insert 12 at pos 1, shift other items up
print mylist
print mylist.count(12) # How many times is 12 in mylist?
mylist.extend([5, 9, 5, 11]) # Put whole list onto end of mylist
print mylist
print mylist.index(9) # Find index of first 9 in mylist
mylist.reverse() # Flips the list
print mylist
mylist.sort() # Organizes in numerical order
print mylist
mylist.remove(12) # Remove the first 12 in the lis
print mylist

print '' # How to unpack lists in lists
steve = [1, 2, 3]
ron = ['Hi', 'Corn', steve]
t = ron[2]
print t[1]

print ''
mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print mx[1][2] # Row and then column
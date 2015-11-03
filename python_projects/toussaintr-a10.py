#-######################################################################
# Author: Roland Junior Toussaint
#
# username: toussaintr
#
# Assignment: A10
#
# Purpose: Gain additional practice working with strings to do something useful
# and work on using functions to step through strings.
########################################################################
# Acknowledgements:
# Html code provided by Jan Pearce from
# http://cs.berea.edu/courses/csc226/tasks/basic.html
######################################################################

def br_fix(broken_html, fixed_html, start):
    """ This function takes the parameters of the code needing to be fixed,
    the new blank docstring, and a number to start walking through the code at.
    This takes the html given and walks through it looking for < br, hr, img, or
    meta. If it encounters these it steps through till the > and replaces it with
    ' />'. After steping through the html it returns the new fixed code."""
    while start < len(broken_html): # runs through the entire string and stops at the end
        letter = broken_html[start] # sets letter to the new current letter in docstring
        fixed_html += letter # This adds the new letter to the new string
        if letter == '<': # Looks for the value to equal '<'
            start += 1 # Moves it to the next letter in the string
            letter = broken_html[start]
            fixed_html += letter
            if letter == 'b' or letter == 'h' or letter == 'i' or letter == 'm': # Looks ofr b h i m
                start += 1
                letter = broken_html[start]
                fixed_html += letter
                if letter == 'r' or letter == 'm'or letter == 'e': # looks for r m e
                    start += 1
                    letter = broken_html[start]
                    if letter == 'a': # Looks for a
                        fixed_html += letter
                    else: # if not a
                        if letter != '>': # if not > loop until is
                            while letter != '>':
                                 fixed_html += letter
                                 start += 1
                                 letter = broken_html[start]
                        if letter == '>': # once it is print  /> in its place
                            letter = broken_html[start]
                            fixed_html += ' />'

        start += 1 # steps threw letters if not <
    return fixed_html # gives back the fixed html
################################################################################
# this is the broken code to fix
broken_html = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta content="text/html;charset=UTF-8" http-equiv="Content-Type">
  <title>Basic Web Page</title>
</head>
<body>
<h3>A Basic Web Page</h3>

<p>A basic web page looks something like this. It might have
images like:<br>

<img style="width: 66px; height: 44px;" alt="WC3 image" src="wc3.gif">
<br>
And it might have a line like:
</p>

<hr>
<p>Be sure to "view source" of this page.</p>
</body>
</html>'''

# this tells where to start in the string
start = 0
# Creates a new docstring that the fix code will be added to
fixed_html = ""

# Makes the function return = fixed_html
fixed_html = br_fix(broken_html, fixed_html, start)

# print the fixed code
print fixed_html





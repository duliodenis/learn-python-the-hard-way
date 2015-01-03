#
#  ex13c.py (Parameters, Unpacking, Variables)
#  Python the Hard Way Exercise #13 - Part c
#
#  Created by Dulio Denis on 1/2/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex13.html
#
from sys import argv

# this version of the exercise will take four arguments
script, first, second, third, fourth = argv

# and a fifth from the user
fifth = raw_input("Enter a fifth argument:")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your fifth variable is:", fifth
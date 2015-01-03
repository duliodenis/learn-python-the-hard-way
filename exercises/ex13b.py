#
#  ex13b.py (Parameters, Unpacking, Variables)
#  Python the Hard Way Exercise #13 - Part b
#
#  Created by Dulio Denis on 1/2/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex13.html
#
from sys import argv

# this version of the exercise will take only two arguments
script, first, second = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "There is no third variable"
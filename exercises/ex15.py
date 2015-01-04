#
#  ex15.py (Reading Files)
#  Python the Hard Way Exercise #15
#
#  Created by Dulio Denis on 1/4/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex15.html
#
from sys import argv

# the name of the script and the filename from the argument vector
script, filename = argv
txt = open(filename)

print "Here is your file: %r" % filename
print txt.read()
txt.close()

print "Type the filename again:"
fileAgain = raw_input("> ")
txtAgain = open(fileAgain)

print "The first line of the file is:"
print txtAgain.readline()
txtAgain.close()
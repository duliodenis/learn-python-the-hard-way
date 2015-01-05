#
#  ex16.py (Reading and Writing Files)
#  Python the Hard Way Exercise #16
#
#  Created by Dulio Denis on 1/5/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex16.html
#
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#don't need truncate() with 'w' option.
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close the file."
target.close()
#
#  ex05.py
#  Python the Hard Way Exercise #5
#
#  Created by Dulio Denis on 12/25/14.
#  Copyright (c) 2014 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex5.html
#
# Set-up the variables
name = "Dulio"
age = 35 # Not a lie
height = 71 # inches
weight = 190 # lbs
eyes = "Black"
hair = "Red"
teeth = "white"

# The String Outputs with format specifiers
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."

print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the tea." % teeth

# The tricky line
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age+height+weight)

# The %r format specifier
print "The raw value of weight is %r" % weight

# Some unit conversion: height into feet and inches
feet = height / 12
inches = height % 12
print "I am %d feet and %d inches tall." % (feet, inches)

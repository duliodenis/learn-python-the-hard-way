#
#  ex11.py (Asking Questions)
#  Python the Hard Way Exercise #11
#
#  Created by Dulio Denis on 12/31/14.
#  Copyright (c) 2014 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex11.html
#
#print "How old are you?",
age = raw_input("How old are you?")
#print "How tall are you?",
height = raw_input("How tall are you?")
#print "How much do you weigh?",
weight = raw_input("How much do you weigh?")

birthday = raw_input("When is your birthday?\n")

print "So, you are %r old, %r tall, and %r heavy" % (
	age, height, weight)
print "and your birthday is on %r" % birthday
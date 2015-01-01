#
#  ex12.py (Prompting People)
#  Python the Hard Way Exercise #12
#
#  Created by Dulio Denis on 1/1/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex12.html
#
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r years old, %r tall, and you weigh %r." % (
	age, height, weight)
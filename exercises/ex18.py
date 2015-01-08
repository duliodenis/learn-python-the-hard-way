#
#  ex18.py (Names, Variables, Code, Functions)
#  Python the Hard Way Exercise #18
#
#  Created by Dulio Denis on 1/7/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex18.html
#
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
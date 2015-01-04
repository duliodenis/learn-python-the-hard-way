#
#  ex14.py (Parameters, Unpacking, Variables)
#  Python the Hard Way Exercise #14
#
#  Created by Dulio Denis on 1/3/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex14.html
#
from sys import argv

script, userName, game = argv
prompt = '$: '

print "Hi %s, I'm the %s script." % (userName, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % userName
likes = raw_input(prompt)

print "Where do you live %s" % userName
location = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
It's good that your favorite game is %r.
""" % (likes, location, computer, game)

# Play Zork at:
# http://thcnet.net/zork/index.php
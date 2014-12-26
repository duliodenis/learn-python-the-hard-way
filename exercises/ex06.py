#
#  ex06.py (Strings & Text)
#  Python the Hard Way Exercise #6
#
#  Created by Dulio Denis on 12/26/14.
#  Copyright (c) 2014 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex6.html
#
typesOfPeople = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
knowDontKnow = "Those who know %s and those who %s." % (binary, doNot)

print typesOfPeople
print knowDontKnow

print "I said: %r" % typesOfPeople
print "I also said: '%s'." % knowDontKnow

hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"

print jokeEvaluation % hilarious

leftSide = "This is the left side of ..."
rightSide = " a string with a right side."

print leftSide + rightSide


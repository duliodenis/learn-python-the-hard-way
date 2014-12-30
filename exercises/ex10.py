#
#  ex10.py (What Was That?)
#  Python the Hard Way Exercise #10
#
#  Created by Dulio Denis on 12/30/14.
#  Copyright (c) 2014 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex10.html
#
tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."

fatCat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

rawFormatter = "%r - %r"
stringFormatter = "%s - %s"

tripleFatCat = '''
I can "include" double quotes.
And that is a "great" thing.
'''

tripleFatCat2 = '''
and one more double "quote" line.
'''

bellCat = "\a"

print tabbyCat
print persianCat
print backslashCat
print fatCat
print ""
print rawFormatter % (tripleFatCat, tripleFatCat2)
print ""
print stringFormatter % (tripleFatCat, tripleFatCat2)
print bellCat

# Extra fun
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,
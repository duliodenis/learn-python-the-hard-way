#
#  ex08.py (Printing, Printing)
#  Python the Hard Way Exercise #8
#
#  Created by Dulio Denis on 12/28/14.
#  Copyright (c) 2014 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex8.html
#
# Set-up the formatter string
formatter = "%r %r %r %r"
# An alternate formatter
formatterPipes = "(%r | %r | %r | %r)"

print formatter % (1,2,3,4)
print formatterPipes % (1,2,3,4)

print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type upright.",
	"But it didn't sing.",
	"So I said goodnight."
)
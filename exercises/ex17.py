#
#  ex17.py (More Files)
#  Python the Hard Way Exercise #17
#
#  Created by Dulio Denis on 1/6/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex17.html
#
from sys import argv
from os.path import exists

script, fromFile, toFile = argv

# print "Copying from %s to %s" % (fromFile, toFile)
inData = open(fromFile).read()

# print "The input file is %d bytes long" % len(inData)
# print "Copying %d bytes from %s to %s" % (len(inData), fromFile, toFile)
# print "Does the output file exist? %r" % exists(toFile)

if exists(toFile):
	print "Copying %d bytes from %s to current file %s" % (len(inData), fromFile, toFile)
else:
	print "Copying %d bytes from %s to new file %s" % (len(inData), fromFile, toFile)
	
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

outFile = open(toFile, 'w')
outFile.write(inData)

print "Copy complete."
outFile.close() 
#
#  ex04.py
#  Python the Hard Way Exercise #4
#
#  Created by Dulio Denis on 12/24/14.
#  Copyright (c) 2014 ddApps. All rights reserved.
# ------------------------------------------------
#

# Set-up the Variables
cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90
carsNotDriven = drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePassengersPerCar = passengers / carsDriven

# Print the results
print "There are", cars,"cars available."
print "There are only", drivers,"drivers available."
print "There will be", carsNotDriven,"empty cars today."
print "We can transport", carpoolCapacity,"people today."
print "We have", passengers,"to carpool today."
print "We need to put about", averagePassengersPerCar,"in each car."
 
##########
#
# STEP 3.1: ERROR HANDLING - Basic message pop.
# Copy this code into an extensions script bit by bit from the top down to see how it all works. Use the test button to see what comes up in
#
##########

#For this we'll need to import the from System.Windows import * method
from System.Windows import *

#create MessageBox
def displayMessage(message):
	MessageBox.Show(str(message))

###
#If/else statement
###

value = 100

if value < 1000:
	displayMessage("Value is less than 1000")
else:
	displayMessage("Value is equal to or greater than 1000")
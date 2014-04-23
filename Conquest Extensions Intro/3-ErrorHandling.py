##########
#
# STEP 3: ERROR HANDLING
# Copy this code into a console bit by bit from the top down to see how it all works.
#
##########

###
#Basic TRY/CATCH statement.
###
try:
	test = 1 / 0 #will not work
except Exception, e:
	print "There is an error: " + e.message #and here we print the resulting error message, which in this case will be: 'There is an error: Attempted to divide by zero.'

###
#Error message - Let's create a function that makes it simpler to display a message box when something's not quite right. Also very useful for testing.
###

#For this we will have to import the Conquest namespace, which will enable us to use the 'ErrorMessageException' function.
from Conquest import *

#Let's create a function that will display the message we tell it to in a popup ErrorMessageException. For example error("Error message"). This is the right way to display an error box in a Conquest Extension.
def error(o):
	raise ErrorMessageException(str(o))

#here we create an if statement to display one or the other
if 10 == 9:
	error("10 equals 9.")
else:
	error("10 doesn't equal 9.") #this ErrorMessageException will display.
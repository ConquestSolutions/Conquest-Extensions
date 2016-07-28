##########
#
# ERROR HANDLING - Raise Exception, log exception in log file
# Copy this code into an extensions script bit by bit from the top down to see how it all works. Use the test button to see what comes up in
#
##########

#For this we will have to import the Conquest namespace, which will enable us to use the 'ErrorMessageException' function.
from Conquest import *

#Let's create a function that will display the message we tell it to in a popup ErrorMessageException. For example error("Error message"). This is the right way to display an error box in a Conquest Extension.
def error(message):
	raise ErrorMessageException(message)
	
#here we create an if statement to display one or the other
if 10 != 9:
	error("10 doesn't equal 9.")
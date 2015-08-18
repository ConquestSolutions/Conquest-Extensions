##########
#
# STEP 3.1: MESSAGE BOX - Basic message pop.
# Copy this code into an extensions script bit by bit from the top down to see how it all works. Use the test button to see what comes up in
#
##########

#For this we'll need to import the from System.Windows import * method
from System.Windows import *

#create a reusable MessageBox
def displayMessage(message):
	MessageBox.Show(str(message))

###
#If/else statement
###

value = 100

if value < 1000:
	displayMessage("Value '" + str(value) + "' is less than 1000")
else:
	displayMessage("Value '" + str(value) + "' is equal to or greater than 1000")

#create a dictionary with keys and values
user = {
	'firstName': 'Person',
	'lastName': 'A',
	'phoneNumber' : 123456789,
	'email' : 'testemail@example.com',
	'username' : 'PersonA'
	}

#print some contact details using the keys
sentence = 'You can call ' + user['firstName'] + ' on ' + str(user['phoneNumber']) + ' or email at ' + user['email'] + '.'

#display the message
displayMessage(sentence)
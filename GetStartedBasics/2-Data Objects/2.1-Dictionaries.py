##########
#
# STEP 2: THIS SCRIPT SHOWS HOW TO CREATE DICTIONARIES
# Copy this code into a script to see how to create a key value pair dictionary.
##########

#create a dictionary with keys and values
user = {
	'firstName': 'Person',
	'lastName': 'A',
	'phoneNumber' : 123456789,
	'email' : 'testemail@example.com',
	'username' : 'PersonA'
	}

#print the dictionary
print user

#print some contact details using the keys
sentence = 'You can call ' + user['firstName'] + ' on ' + str(user['phoneNumber']) + ' or email at ' + user['email'] + '.'
print sentence
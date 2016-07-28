##########
#
# THIS SCRIPT IS A LITTLE BASIC PYTHON IN THE CONTEXT OF THE CONQUEST EXTENSIONS CONSOLE
# Copy this code into a console bit by bit from the top down to see how it all works.
#
##########

#Declare variable (change to your favourite number!)
variable = 37

#Return variable
print 'Variable: ' + str(variable)

#Multiply variable and return it
multipliedVariable = 9 * variable
print 'Multiplied variable: ' + str(multipliedVariable)

#Adding to a variable string is also easy
companyName = 'companyName'
companyName += ' '
companyName += 'companyName'
print 'Company Name: ' + companyName

#Create a reusable function - this function takes two arguments - team name and team nickname. It then joins them together in a string and prints the result.
def printName(firstName, lastName):
     print 'Full Name: ' + firstName + ' ' + lastName

printName('Person', 'A') #returns 'FirstName LastName'
printName('Person', 'B')

#IF STATEMENT
#This statement will return TRUE as 'a' is bigger than 'b'
a = 100
b = 2

if (a>b):
	print 'a is bigger than b' #This will return true
else:
	print 'a is not bigger than b'
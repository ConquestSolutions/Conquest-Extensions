##########
#
# STEP 1: THIS SCRIPT IS A LITTLE BASIC PYTHON IN THE CONTEXT OF THE CONQUEST EXTENSIONS CONSOLE
# Copy this code into a console bit by bit from the top down to see how it all works.
#
##########

#Declare variable (change to your favourite number!)
variable = 37

#Return variable
print 'Variable: ' + variable

#Multiply variable and return it
multipiedvariable = 9 * variable
print 'Multiplied variable: ' + multipiedvariable

#Adding to a variable string is also easy
conquest = 'conquest'
conquest += ' '
conquest += 'solutions'
print 'Conquest: ' + conquest

#Create a reusable function - this function takes two arguments - team name and team nickname. It then joins them together in a string and prints the result.
def aflTeam(name, nickname):
     print 'AFL Team: ' + name + ' ' + nickname

aflTeam('Adelaide','Crows') #returns 'Adelaide Crows'

#IF STATEMENT
#This statement will return TRUE as 'a' is bigger than 'b'
a = 100
b = 2

if (a>b):
	print 'TRUE' #This will return true
else:
	print 'FALSE'
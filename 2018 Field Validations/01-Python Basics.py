
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

#create a list and add to it using '.append'
newList = ['Item 1', 'Item 2', 'Item 3']
for listItem in newList:
	print listItem

#add more items
newList.append("Item 4")
newList.append("Item 5")
newList.append("Item 6")

#For each item in newList, it will print the item.
for listItem in newList:
	print listItem
##########
#
# STEP 2: THIS SCRIPT SHOWS HOW TO CREATE LISTS
# Copy this code into a console bit by bit from the top down to see how it all works.
#
##########

#create a list and add to it using '.Add'
dotnetList = List[str](['Item 1', 'Item 2', 'Item 3'])
dotnetList.Add("Item 4")
dotnetList.Add("Item 5")
dotnetList.Add("Item 6")
print dotnetList

#For each item in dotnetList, it will print the item.
for s in dotnetList:
	print s
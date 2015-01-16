##########
#
# STEP 6.1: THIS SCRIPT CREATS A BUTTON WHICH CHECKS IF THERE ARE ADDRESS FIELDS ENTERED, AND IF SO GENERATES A LOCATION STRING AND PLACES IT IN THE LOCATION FIELD
# Copy this code into RequestLoadInterfaceContent.
#
#NOTE: To test this, you'll need to save the script and then open up an request. There you'll see a button.
#      Add some address values and watch it assign a location field.
#
##########

#import name spaces which contain the UI buttons and peripherals
from System import String
from System.Windows import *
from System.Windows.Controls import *

#create MessageBox functionality
def displayMessage(message):
	MessageBox.Show(str(message))

#write a function that does what we want the button to do when it is clicked
def btnGenerateLocationClick(sender, e):

	#generate the string we want to input into the location field
	Location = ''
	if not String.IsNullOrWhiteSpace(source.Address):
		Location = str(source.Address) + ' \n'
	if not String.IsNullOrWhiteSpace(source.Suburb):
		Location += str(source.Suburb) + ' \n'
	if not String.IsNullOrWhiteSpace(source.PostCode):
		Location += str(source.PostCode) + ' \n'

	#assign source.Location the new Location string if it's not empty
	if not String.IsNullOrWhiteSpace(Location):
		source.Location = Location
	else:
		displayMessage("There's no data to pop the location field with.")

def loadButton():
	#create a button. 'Button()' is a standard control we can use. we then give it a string to display, and then assign the event function we created earlier
	locationButton = Button()
	locationButton.Content = "Generate Location"
	locationButton.Click += btnGenerateLocationClick

	#Add the button to a panel. Here we get the button we created and add it to the panel.
	panel = StackPanel()
	panel.Children.Add(locationButton)
	panel.Margin = Thickness(2,2,2,2)

	#Add the Panel to the User Interface so it displays when an request loads.
	source.InterfaceContent = panel

loadButton()
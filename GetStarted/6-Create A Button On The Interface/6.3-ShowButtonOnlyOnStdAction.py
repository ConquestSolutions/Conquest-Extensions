##########
#
# STEP 6.3: CHECKS IF AN ACTION IS A PARTICULAR STANDARD ACTION
# use this if you'd like to perform code on an action with a particular StdAction type
# Copy this code into the client side script with scriptkey:
# ActionLoadInterfaceContent
#
##########

from System import *
from System.Windows import *
from System.Windows.Controls import *
from Conquest.Silverlight import *
from Conquest.Security import *

#select StdActionID to display message box on
StdActionID = 173

#create a reusable MessageBox
def displayMessage(message):
	MessageBox.Show(str(message))

def btnShowVandalism(sender, e):
	#show message box saying it is a Vandalism action
	displayMessage('ActionID ' + str(source.ActionID) +' is a vandalism action.')

#create a button and run the function btnShowVandalism() when clicked
def loadButton():
	vandalismBtn = Button()
	vandalismBtn.Content = "Vandalism"
	vandalismBtn.Click += btnShowVandalism

	#Add the button to a panel. Here we get the button we created and add it to the panel.
	panel = StackPanel()
	panel.Children.Add(vandalismBtn)
	panel.Margin = Thickness(2,2,2,2)

	#Add the Panel to the User Interface so it displays when the action loads.
	source.InterfaceContent = panel

#only load the button if the action meets the criteria
if source.StdActionID == StdActionID:	
	loadButton()
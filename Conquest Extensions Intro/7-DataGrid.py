##########
#
# STEP 7: OPEN AND POPULATE A DATA GRID
# Copy this code into any interface scripts such as the 'RequestLoadInterface' script. All this code does is open up a datagrid and populate it with data from tblSystem.
#
##########

#import required name spaces which contain the UI buttons and peripherals
from System.Windows import *
from System.Windows.Controls import *
from Conquest import *
from Conquest.Silverlight import *
from Conquest.Silverlight.Common import *
from Conquest.Silverlight.Controls import *

#initialise the datagrid, make the cells 'readonly' and specify the height
dataGrid = CQDataGrid()
dataGrid.IsReadOnly = True;
dataGrid.MaxHeight = 300

#initialise the window that the datagrid will sit inside, give it a button to close, and specify we wish the content to be the dataGrid we created
childWindow = CQChildWindow()
childWindow.HasCloseButton = True
childWindow.Content = dataGrid

#specify a function - what we want to do with the data when the query is complete (read down for this to make sense)
#populate the datagrid with the data from the query and then show the childWindow (which has the grid in it)
def runQuery_Callback(records):
    dataGrid.ItemsSource = records
    childWindow.Show()

#event that happens when the button is clicked, runs the query and then run the callback that we just created above
def btn_RunQuery(sender, e):
    App.RunQuery("Select * From tblSystem", runQuery_Callback)

#create the button and assign the RunQuery Event to it.
lnkButton = Button()
lnkButton.Content = "System Options"
lnkButton.Click += btn_RunQuery

#add the button to the stack panel
panel = StackPanel()
panel.Children.Add(lnkButton)
panel.Margin = Thickness(2,2,2,2)

#add the stack panel to the user interface
source.InterfaceContent = panel

#fires the window in test mode so we dont have to create a new request to test each time
if (IsTestMode):
	btn_RunQuery(None, None)

####  Simple Lookup
from Conquest.Silverlight.Controls import *

def grid_RowDoubleClick(_, e) :
	global popWindow
	popWindow.Close()
	source.Account = e.Data

def showGrid(items) :
	global popWindow
	
	dg = CQDataGrid()
	dg.MaxHeight = 300
	dg.IsReadOnly = True
	dg.GridRowDoubleClick += grid_RowDoubleClick
	dg.ItemsSource = items

	popWindow = CQChildWindow()
	popWindow.HasCloseButton = True
	popWindow.Title = "Double-click a item to select"
	popWindow.Content = dg
	popWindow.Show()

if LookupRequested or IsTestMode :
	showGrid(['Item 1', 'Item 2', 'Item 3'])


#### Lookup with service call
#https://jsonplaceholder.typicode.com/users
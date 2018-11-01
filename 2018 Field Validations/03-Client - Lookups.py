
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
from Conquest.Silverlight.Controls import *
from Conquest.Silverlight import *

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

def QueryServiceApi():
	serverCode = """
import json
from System.Net import WebClient
from Conquest import ObjectHelper
client = WebClient()
jsonStr = client.DownloadString(url)
jsonList = json.loads(jsonStr)
output = ObjectHelper.ConvertToString(jsonList)
	"""

	def error_CallBack(error):
		print(error)
		App.CloseWait()
		
	def runScript_CallBack(result):
		import clr
		from Conquest import ObjectHelper
		list = ObjectHelper.ConvertToObject(result, clr.GetClrType(type([])))
		convertedList = []
		for item in list:
			convertedList.append(str(item["name"]))
		App.CloseWait()
		showGrid(convertedList)
		
	App.RunScriptOnServer(runScript_CallBack, error_CallBack, serverCode, "url", "https://jsonplaceholder.typicode.com/users")
	App.PopWait()


if LookupRequested or IsTestMode :
	QueryServiceApi()
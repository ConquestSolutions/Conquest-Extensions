from Conquest.Silverlight import *


#simple validation
if source.Account == None or source.Account == "" :
	callBack('Account is empty.')

#validation with user interaction
def Should_Continue_Handler(_, e):
	if e.DialogResult == DialogResult.False:
		callBack("You choose not to continue.")
	else:
		callBack(None)
		
if source.Account == None or source.Account == "" :
	isWaitCallBack = True
	MessagePop.Show("Account is empty, are your sure to continue?", MessageButtons.YesNo, Should_Continue_Handler)

#validation with query
def query_callback(result):
	if len(result) > 0:
		testValue = next(iter(result)).TestValue
		print testValue
		if testValue.startswith("Mum"):
			callBack(testValue)
		else:
			callBack(None)
	else:
		callBack(None)
App.RunQuery("SELECT 'Mum says no.' AS TestValue", query_callback)
isWaitCallBack = True


#validation with third-party services
serverCode = """
import json
from System.Net import *

client = WebClient()
jsonStr = client.DownloadString(url)
result = json.loads(jsonStr)
output = result["title"]
"""

def error_CallBack(error):
	callBack(error)
	
def runScript_CallBack(result):
	callBack(result)
	
App.RunScriptOnServer(runScript_CallBack, error_CallBack, serverCode, "url", "https://jsonplaceholder.typicode.com/todos/1")
isWaitCallBack = True
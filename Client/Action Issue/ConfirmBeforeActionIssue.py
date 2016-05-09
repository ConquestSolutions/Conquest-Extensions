## ScriptKey: ActionLoadInterfaceContent, tested on 3.0329

###

DEBUG = True # if true show debug messages. Turn this off when satisfied.

###

import clr
clr.AddReference("System.Core")
import System
clr.ImportExtensions(System.Linq)
from System.Linq import Enumerable
from System.Windows.Controls import StackPanel, Button
from Conquest.Silverlight import MessagePop, DialogResult, MessageButtons, MessageIcons
from System.Windows.MessageBox import Show

## Utilities

def debug(o):
	if DEBUG: Show(str(o))
	
def confirm(message, action, buttons = MessageButtons.YesNo, icons = MessageIcons.Warning):
	def onDialogResult(sender, args):
		if args.DialogResult == DialogResult.True:
			action()
	MessagePop.Show((message or "").strip(), "Confirm", buttons, icons, onDialogResult)

def makeButton(name, action):
	B = Button()
	B.Content = name
	B.Height = 35
	B.Background = None
	def B_OnClick(sender, e):
		action()
	B.Click += B_OnClick
	return B

def getUserProgramPanel():
	"""
	Get the StackPanel for where user programs are put
	"""
	if not hasattr(source, "InterfaceContent"):
		debug("Expected model to have InterfaceContent")
		return None
	
	P = source.InterfaceContent
	if not P:
		P = StackPanel()
		source.InterfaceContent = P
		return P
	
	t = P.GetType()
	if t.Name == "StackPanel":
		return P
	
	debug("Expected StackPanel for UserPrograms control, found " + P.GetType().Name)
	return None

def setUserProgram(name, action):
	"""
	Put a button in user programs that executes `action`
	Returns True if set
	"""
	P = getUserProgramPanel()
	if not P: return False

	B = Enumerable.OfType[Button](P.Children).FirstOrDefault(lambda b: b.Content == name)
	
	if B:
		P.Children.Remove(B)
	
	if action:
		B = makeButton(name, action)
		P.Children.Add(B)
		return True
	
	debug("setUserProgram: not set %1" % str(name))
	return False

## Business Code

def replaceActionIssueTask():
	"""
	Disable the existing Work Order task and our custom one.
	"""
	if hasattr(model, "IssueWorkOrder"):
		if setUserProgram("Issue Work Order", confirmIssueWorkOrder):
			model.HideMenu("Action>Issue Work Order")
			return True
	return False


RailSafetyCertificateMessage = """
You are issuing work to someone not recorded as having a Rail Safety Certificate.

Do you want to continue?
"""

def hasRailSafetyCertificate():
	return (source.UserText1 or "").lower() == "rsc=yes"

def confirmIssueWorkOrder():
	if hasRailSafetyCertificate():
		model.IssueWorkOrder()
	else:
		confirm(RailSafetyCertificateMessage, model.IssueWorkOrder)
	
replaceActionIssueTask()
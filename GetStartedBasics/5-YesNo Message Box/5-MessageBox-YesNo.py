##########
#
# STEP 5: THIS SCRIPT BUILDS A BASIC MESSAGE BOX THAT GIVES THE USER A YES OR NO OPTION
# Copy this code into any client side script (ie Action Saving Validation).
#
### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionSavingValidation' FOR IT TO WORK
#
##########

from System import *
from System.Windows import *
from Conquest.Silverlight import *

def done(): callBack(None)
def fail(s): callBack(s)

def MessagePop_Handler(s5,e):
    if e.DialogResult == DialogResult.False:
        fail("You clicked no!")
    else:
    	done()

#Validate a field - check that a location has been entered, if it hasn't, display a warning box
if String.IsNullOrWhiteSpace(source.Location):
	isWaitCallBack = True
	MessagePop.Show("The location field is empty, do you still want to save?", MessageButtons.YesNo, MessagePop_Handler)
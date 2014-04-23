##########
#
# STEP 5: THIS SCRIPT BUILDS A BASIC MESSAGE BOX THAT GIVES THE USER A YES OR NO OPTION
# Copy this code into any script.
#
##########

#Import namespaces. These are required for certain features to execute properly.
from Conquest import *
from Conquest.Silverlight import *

#initiate wait for callback before doing anything
isWaitCallBack = True

def MessagePop_Handler(s5,e):
    if e.DialogResult == DialogResult.True:
        callBack("You clicked yes! :)")
    else:
        callBack("You clicked no! :(")

#fire MessagePop - MessagePop.Show(MessageToShow, MessageButtonsToDisplay, MessagePopHandlerForYesAndNo)
MessagePop.Show("Are you sure you want to save?", MessageButtons.YesNo, MessagePop_Handler)
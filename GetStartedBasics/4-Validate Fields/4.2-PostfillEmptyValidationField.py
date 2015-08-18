##########
#
# STEP 4: THIS SCRIPT VALIDATES THE LOCATION FIELD IN THE ACTION FORM BEFORE IT FIRES
# Copy this code into ActionSavingValidation - it uses the location field from that particular interface.
# This script fires when someone goes to 'save' an action. We want to check to make sure they have entered a location.
# Alternatively, instead of providing an error message, we could populate it ourselves to a generic location.
#
### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionSavingValidation' FOR IT TO WORK
#
##########

from System import *
from System.Windows import *

#create reusable MessageBox
def displayMessage(message):
	MessageBox.Show(str(message))

#Alternatively, instead of providing an error message, we could populate it ourselves to a generic location.
if String.IsNullOrWhiteSpace(source.Location):
	source.Location = 'Melbourne'
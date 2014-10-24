##########
#
# STEP 4: THIS SCRIPT VALIDATES THE LOCATION FIELD IN THE ACTION FORM BEFORE IT FIRES
# Copy this code into ActionSavingValidation - it uses the location field from that particular interface.
# This script fires when someone goes to 'save' an action. We want to check to make sure they have entered a location.
# Check first two characters of field
#
##########

### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionSavingValidation' FOR IT TO WORK

#import the relevant namespaces
from System import *
from System.Windows import *
from Conquest import *
from Conquest.DataAccess import *

#create MessageBox
def displayMessage(message):
	MessageBox.Show(str(message))

#Check to see if the first 8 characters of the string 'Location' equal CONQUEST
if source.Location[:8] != 'CONQUEST':
	isWaitCallBack = True
	displayMessage('Not correct format - please prefix with CONQUEST')
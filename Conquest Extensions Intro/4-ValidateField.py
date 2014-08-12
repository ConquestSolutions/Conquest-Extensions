##########
#
# STEP 4: THIS SCRIPT VALIDATES THE LOCATION FIELD IN THE ACTION FORM BEFORE IT FIRES
# Copy this code into ActionSavingValidation - it uses the location field from that particular interface.
# This script fires when someone goes to 'save' an action. We want to check to make sure they have entered a location.
#
##########

### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionSavingValidation' FOR IT TO WORK

#import the relevant namespaces
from System import *
from System.Windows import *
from Conquest import *
from Conquest.DataAccess import *

entity = Connection.Entities
if IsTestMode:
	source = entity.LoadAsset(14592)

#create MessageBox
def p(o):
	MessageBox.Show(str(o))

#Validate a field - check that a location has been entered, if it hasn't display a messagebox.
if String.IsNullOrWhiteSpace(source.Location):
	isWaitCallBack = True #isWaitCallback is a Conquest function that will prevent the 'Save' from firing until it gets a callback.
	p('Please enter a location.')

#Alternatively, instead of providing an error message, we could populate it ourselves to a generic location.
if String.IsNullOrWhiteSpace(source.Location):
	source.Location == 'Melbourne'

#Check first two characters of field
if source.UserText1[:2] != 'MS':
	isWaitCallBack = True
	p('Not correct format')
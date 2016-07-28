##########
#
# THIS SCRIPT DISABLES A MENU ITEM ON AN ACTION BASED UPON WHETHER THE USER IS AN ADMIN
# Use User Roles for more comprehensive control
# Copy this code into the client side script with scriptkey:
# script key: ActionLoadInterfaceContent
#
##########

from System import *
from Conquest.Silverlight import *
from Conquest.Security import *

#get your user levels
user = UserProfile.CurrentUser
userAdmin = user.ConquestAdministrator

#check if you are an admin in test mode	
if IsTestMode:
	print "Are you an administrator? " + str(userAdmin)

#If you are an admin, you won't see the following options. (If you are not admin, change to False)
if userAdmin == True:
	model.DisableMenu("Action>Copy Action")
	model.DisableMenu("Action>Move Action")
	model.DisableMenu("Action>Delete")
	model.DisableMenu("Action>Assign Standard Action")
	model.DisableMenu("Action>Request Approval")
	model.DisableMenu("Action>Relate Requests")
	model.DisableMenu("Action>Relate Defects")
	model.DisableMenu("Action>Complete")
##########
#
# STEP 8.2: THIS SCRIPT HIDES A MENU ITEM ON AN ACTION BASED UPON WHETHER THE USER IS AN ADMIN  
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
	model.HideMenu("Action>Copy Action")
	model.HideMenu("Action>Move Action")
	model.HideMenu("Action>Delete")
	model.HideMenu("Action>Assign Standard Action")
	model.HideMenu("Action>Request Approval")
	model.HideMenu("Action>Relate Requests")
	model.HideMenu("Action>Relate Defects")
	model.HideMenu("Action>Complete")
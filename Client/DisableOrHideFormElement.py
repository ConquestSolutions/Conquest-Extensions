#sample code to disable or hide menu items in asset form
#script key: AssetLoadInterfaceContent

from System import *
from Conquest.Silverlight import *
from Conquest.Security import *

user = UserProfile.CurrentUser

if IsTestMode:
	#query user profile
	print user.UserName
	
	#check is administrator
	if user.ConquestAdministrator:
		print "is Administrator"
	
	#check object permission
	print "Asset Permission (user): " + str(user.SecurityObjects.AssetRegistor)
	print "Asset Permission (current asset): " + str(source.Permission)
	
	#check user's role information
	for role in user.LicGroups:
		print role.GroupName

#disable for all scenarios
model.DisableMenu("Asset>New>Master Action")

#hide menu for all scenarios
model.HideMenu("Asset>New>Request")

#disable/hide sub-menu (lower part)
model.DisableSubMenu("Asset>Delete Asset")
model.HideSubMenu("Asset>Select All")
model.DisableSubMenu("Document>Delete")
model.DisableSubMenu("Document>View In Trim")

#disable new standard action menu
model.DisableMenu("Asset>New>Action>Admin")	#Standard Action Description
model.DisableMenu("Asset>New>Action>124")	#Standard Action ID
model.HideMenu("Asset>New>Action>125")
model.HideMenu("Asset>New>Action>126")
model.HideMenu("Asset>New>Action>127")
model.HideMenu("Asset>New>Action>128")
model.HideMenu("Asset>New>Action>129")
model.HideMenu("Asset>New>Action>130")

#disable base on object permission
if source.Permission == PermissionType.ReadOnly:
	model.HideMenu("Asset>New>Asset")

#disable base on user's role
if user.IsRole("Office Administration"):
	model.DisableMenu("Asset>New>Master Action")
	model.DisableMenu("Asset>New>Defect")
	model.DisableMenu("Asset>New>Action")

#hide section
model.HideSection("Notes")
#model.HideSection("Action Details")

#hide tab 
model.HideTab("Costs")
model.HideTab("Diary")
model.HideTab("Completion")
model.HideTab("Documents")
model.HideTab("Estimates and Costs")


#hide field
model.HideField("Asset")
model.HideField("Asset Type")
model.HideField("Location")
model.HideField("Planned Start")
model.HideField("Planned Finish")

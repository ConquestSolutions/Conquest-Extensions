##########
#
# THIS SCRIPT VALIDATES THE LOCATION FIELD IN THE ACTION FORM BEFORE IT FIRES
# Copy this code into ActionIssueValidation - it uses the location field from that particular interface.
# This script fires when someone goes to 'issue' an action.
#
### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionIssueValidation' FOR IT TO WORK
#
##########

#If no Location has been supplied, automatically give it a predetermined value
if String.IsNullOrWhiteSpace(source.Location):
	source.Location = 'Melbourne'

# This time we need to explicitly save the changes to the ObjectContext (but not in TestMode!)
if not IsTestMode:
	source.ObjectContext.SaveChanges();
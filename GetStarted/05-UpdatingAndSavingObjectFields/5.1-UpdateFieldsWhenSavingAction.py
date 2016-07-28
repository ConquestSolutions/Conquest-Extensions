##########
#
# THIS SCRIPT VALIDATES THE LOCATION FIELD IN THE ACTION FORM BEFORE IT FIRES
# Copy this code into ActionSavingValidation - it uses the location field from that particular interface.
# This script fires when someone goes to 'save' an action. We want to check to make sure they have entered a location.
#
### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionSavingValidation' FOR IT TO WORK
#
##########

#If no Location has been supplied, automatically give it a predetermined value
if String.IsNullOrWhiteSpace(source.Location):
	source.Location = 'Melbourne'
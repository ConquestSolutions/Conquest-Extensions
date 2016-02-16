## Suppose that you are writing an action validation, where the `source` object is an action. 
## Setting the `Completed By` field on the action can be done as follows:

from Conquest.Security.SecurityHelper import CurrentUser

source.CompletedBy = CurrentUser.UserName
import Conquest
import Conquest.DataAccess.Connection as conn
from System import *

def require(ok, requirement):
	if not ok:
		raise Conquest.ErrorMessageException(requirement)

def found(sql):
	return len(list(conn.GetRows(sql))) == 1

## The action completion validation is run on the server after Conquest business rules have been evaluated.
## If an exception raised on the server, the completion process will be cancelled.

action = source

# You can inspect the action to be completed and verify that particular details are filled in.

def hasExpectedDisposalValue():
	if (not action or
		action.ActionType != "Disposal" or 
		not action.UserNumber30 >= 0 or
		not action.AssetID > 0):
		return True

	validMeasurement = "select top 1 1 from tblAsset where AssetID = {aid} and Measurement = {m}".format(
		aid = action.AssetID,
		m = action.UserNumber30)

	return found(validMeasurement)

require(hasExpectedDisposalValue(), "The measurement entered should be {m} for the action '{ref} - {desc}'".format(
	m = action.UserNumber30,
	ref = action.ReferenceID,
	desc = action.ActionDescription))